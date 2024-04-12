from flask import Blueprint, request, render_template, url_for, redirect, flash
from tmdb.search import tv_shows
from controllers.tv import populate_from_tmdb, get_show

# Create a Blueprint for the auth routes
bp = Blueprint("tv", __name__, url_prefix="/tv")


@bp.route("/search", methods=["GET"])
def search():
    """Search for TV Shows"""
    title = request.args.get("title")
    matching_shows = tv_shows(title)

    return render_template("tv.html", shows=matching_shows)


@bp.route("/series", methods=["GET"])
def populate_series():
    """Populate the series data from TMDB to the database"""
    tmdb_series_id = request.args.get("tmdb-id")
    if not tmdb_series_id:
        flash("Please specify a TMDB id")
        return request.url
    series_id = populate_from_tmdb(tmdb_id=tmdb_series_id)
    # return redirect(url_for(series_detail(series_id)))
    if not series_id:
        return "Failed to populate"
    return f"Success populating - {series_id}"


@bp.route("/series/<int:id>", methods=["GET"])
def series_detail(id: int):
    """Retrieve the series detail of a TV series"""
    show = get_show(id)
    return render_template("tv-series-detail.html", series=show)


# @bp.route(
#     "/series/<int:id>/season/<int:season_number>/episode/<int:episode_number>",
#     methods=["GET"],
# )
# def season_detail(id: int, season_number: int, episode_number):
#     """Retrieve season detail of a TV series"""
#     return render_template("tv.html", season=episode)


# @bp.route(
#     "/series/<int:id>/season/<int:season_number>/episode/<int:episode_number>",
#     methods=["GET"],
# )
# def episode_detail(id: int, season_number: int, episode_number):
#     """Retrieve episode detail of a TV series"""
#     return render_template("tv.html", episode=episode)
