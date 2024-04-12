from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    session,
    redirect,
    url_for,
)
from controllers.user import create, verify, get_by_email

# Create a Blueprint for the auth routes
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    # Get data from request - adapted from -> https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    data = request.form
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not create(username=username, password=password, email=email):
        return render_template("register.html"), 400

    return redirect(url_for("auth.login"))


@bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    # Get data from request - adapted from -> https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    data = request.form
    password = data.get("password")
    email = data.get("email")

    if not verify(email=email, password=password):
        return render_template("login.html")

    # Add verified user to new session - adapted from -> https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions
    session["email"] = email
    user_id = get_by_email(email)
    session["id"] = user_id.id

    return redirect(url_for("home.home"))


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": True})
