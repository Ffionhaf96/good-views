from flask import Blueprint, request, render_template
from tmdb.search import movies

# Create a Blueprint for the auth routes
bp = Blueprint("movie", __name__, url_prefix="/movie")


@bp.route("/search", methods=["GET"])
def search():
    title = request.args.get("title")
    matching_movies = movies(title)

    return render_template("movie.html", movies=matching_movies)


# @bp.route("/movie/<int:id>", methods=["GET"])
# def movie_detail(id: int):
#     """Retrieve the detail of a movie"""
#     return render_template("movie-detail.html", movie=movie)
