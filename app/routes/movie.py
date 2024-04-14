from flask import Blueprint, request, render_template, flash, url_for, redirect
from tmdb.search import movies
from controllers.movie import populate_from_tmdb, get_by_id

# Create a Blueprint for the auth routes
bp = Blueprint("movie", __name__, url_prefix="/movie")


@bp.route("/search", methods=["GET"])
def search():
    title = request.args.get("title")
    matching_movies = movies(title)

    return render_template("movie.html", movies=matching_movies)


@bp.route("/movie", methods=["GET"])
def populate_series():
    """Populate the movie data from TMDB to the database"""
    tmdb_series_id = request.args.get("tmdb-id")
    if not tmdb_series_id:
        flash("Please specify a TMDB id")
        return request.url
    movie_id = populate_from_tmdb(tmdb_id=tmdb_series_id)

    if not movie_id:
        return "Failed to populate"
    return redirect(url_for("movie.movie_detail", id=movie_id))


@bp.route("/movie/<int:id>", methods=["GET"])
def movie_detail(id: int):
    """Retrieve the detail of a movie"""
    movie = get_by_id(id)
    return render_template("movie-detail.html", movie=movie)
