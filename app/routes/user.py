from flask import (
    Blueprint,
    request,
    render_template,
    url_for,
    redirect,
    session,
    jsonify,
    flash,
)
import controllers.user
from pathlib import Path
from os import getenv
from uuid import uuid4

# Create a Blueprint for the auth routes
bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<int:id>", methods=["GET"])
def user(id: int):
    if not id:
        id = session.get("id")
    user = controllers.user.get_by_id(id)
    if not user:
        return render_template("404.html"), 404
    following = controllers.user.is_following(
        follower_id=session.get("id"), followee_id=id
    )
    return render_template("user.html", user=user, following=following)


@bp.route("/", methods=["GET"])
def user_self():
    id = session.get("id")
    user = controllers.user.get_by_id(id)
    if not user:
        return render_template("404.html"), 404
    return render_template("user-self.html", user=user)


@bp.route("/", methods=["POST"])
def edit():
    email = session.get("email")
    if not email:
        return redirect(url_for("auth.login"), code=400)

    username = request.form.get("username")
    name = request.form.get("name")

    user = controllers.user.update(
        email=email, username=username, name=name, avatar_path=None
    )
    if not user:
        flash("Couldn't update the user as they don't exist!")
        return redirect(url_for("user.user_self"), code=404)
    return redirect(url_for("user.user_self"), code=302)


@bp.route("/avatar", methods=["POST"])
def change_avatar():
    if "avatar" not in request.files:
        flash("Please upload an avatar file")
        return redirect(request.url)
    file = request.files["avatar"]
    if file.filename == "":
        return redirect(request.url)

    # If the files mimetype doesn't contain some type of image we don't want it.
    if "image/" not in file.mimetype:
        flash("Please upload an image")
        return redirect(request.url)

    try:
        file_path = Path(getenv("IMAGE_UPLOAD_FOLDER"), "avatars", uuid4())
        file.save(file_path)
        controllers.user.update(avatar_path=str(file_path))
        flash("Successfully changed avatar!")
    except FileNotFoundError:
        flash("Sorry, we're having trouble uploading your avatar. Please try again.")

    return redirect(request.url)


@bp.route("/", methods=["DELETE"])
def delete():
    email = request.form.get("email")
    if not controllers.user.delete(email):
        return jsonify({"success": False}), 400
    return jsonify({"success": True})


@bp.route("/follow", methods=["POST"])
def follow():
    follower_id = session.get("id")
    followed_id = request.form.get("id")

    if not controllers.user.follow(follower_id=follower_id, followed_id=followed_id):
        flash("Could not follow user")
    else:
        flash("User is now being followed!")

    return redirect(url_for("user.user", id=followed_id))


@bp.route("/unfollow", methods=["POST"])
def unfollow():
    unfollower_id = session.get("id")
    unfollowed_id = request.form.get("id")

    if not controllers.user.unfollow(
        follower_id=unfollower_id, followed_id=unfollowed_id
    ):
        flash("Could not unfollow user")
    else:
        flash("User has been unfollowed!")

    return redirect(url_for("user.user", id=unfollowed_id))
