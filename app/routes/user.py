from flask import (
    Blueprint,
    request,
    render_template,
    url_for,
    redirect,
    session,
    jsonify,
    flash,
    send_from_directory,
)
import controllers.user
from pathlib import Path
from os import getenv
from uuid import uuid4

# Create a Blueprint for the auth routes
bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<int:id>", methods=["GET"])
def user(id: int):
    user = controllers.user.get_by_id(id)
    if not user:
        return render_template("404.html"), 404
    return render_template("user.html", user=user)


@bp.route("/", methods=["POST"])
def edit():
    email = session.get("email")
    if not email:
        return redirect(url_for("auth.login"))

    username = request.form.get("username")
    name = request.form.get("name")

    user = controllers.user.update(email=email, username=username, name=name)
    if not user:
        flash("Couldn't update the user as they don't exist!")
        return redirect(request.url), 404
    return render_template("user.html", user=user)


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
    follower_email = session.get("email")
    followed_email = request.form.get("email")
    if not controllers.user.follow(
        follower_email=follower_email, followed_email=followed_email
    ):
        return jsonify({"success": False}), 400
    return jsonify({"success": True})


@bp.route("/unfollow", methods=["POST"])
def unfollow():
    follower_email = session.get("email")
    followed_email = request.form.get("email")
    if not controllers.user.unfollow(
        follower_email=follower_email, followed_email=followed_email
    ):
        return jsonify({"success": False}), 400
    return jsonify({"success": True})
