from os import getenv
import requests
from typing import Optional, Tuple
from models.models import Movie


API_BASE_URL = "https://api.themoviedb.org/3/movie/"
API_KEY = getenv("TMDB_API_KEY")


def detail(tmdb_id: int) -> Optional[Tuple[Movie, dict]]:
    """
    Retrieves details for a specific Movie
    """
    movie_detail = requests.get(
        f"{API_BASE_URL}{tmdb_id}",
        params={"append_to_response": "credits", "api_key": API_KEY},
        timeout=2,
    )

    if not movie_detail.ok:
        print("Didn't get show")
        return None

    movie_detail = movie_detail.json()
    genres = [genre.get("name") for genre in movie_detail.get("genres")]

    movie = Movie(
        tmdb_id=movie_detail.get("id"),
        title=movie_detail.get("name"),
        release_date=movie_detail.get("release_date"),
        genres=genres,
        description=movie_detail.get("overview"),
        poster_path=movie_detail.get("still_path"),
        content_type="movie",
        poster_path=movie_detail.get("poster_path"),
        duration_minutes=movie_detail.get("runtime"),
        budget=movie_detail.get("budget"),
        revenue=movie_detail.get("revenue"),
    )

    cast = movie_detail.get("credits").get("cast")
   

    return movie, cast
