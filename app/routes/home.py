from flask import Blueprint, render_template


bp = Blueprint("home", __name__, url_prefix="/home")


@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")
