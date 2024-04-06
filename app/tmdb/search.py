from models.dto import Movie, TVShow
from os import getenv
import requests
from typing import Optional, List

API_BASE_URL = "https://api.themoviedb.org/3/search/"
API_KEY = getenv("TMDB_API_KEY")


def movies(title: str) -> Optional[List[Movie]]:
    """
    Searches for Movies based on a title.
    """
    searched_movie = requests.get(
        f"{API_BASE_URL}movie", params={"query": title, "api_key": API_KEY}, timeout=2
    )

    if not searched_movie.ok:
        return None

    movie_list = []
    for movie in searched_movie.json().get("results"):
        print(movie.get("id"))
        movie_list.append(
            Movie(
                tmdb_id=movie.get("id"),
                overview=movie.get("overview"),
                popularity=movie.get("popularity"),
                poster_path=movie.get("poster_path"),
                title=movie.get("title"),
                release_date=movie.get("release_date"),
            )
        )
    movie_list.sort(
        key=lambda movie: movie.popularity,
    )
    return movie_list


def tv_shows(title: str) -> Optional[List[TVShow]]:
    """
    Searches for a TV Shows based on a title.
    """
    searched_show = requests.get(
        f"{API_BASE_URL}tv", params={"query": title, "api_key": API_KEY}, timeout=2
    )

    if not searched_show.ok:
        print("Didn't get show")
        return None

    tv_list = []
    for show in searched_show.json().get("results"):
        tv_list.append(
            TVShow(
                tmdb_id=show.get("id"),
                overview=show.get("overview"),
                popularity=show.get("popularity"),
                poster_path=show.get("poster_path"),
                name=show.get("name"),
                first_air_date=show.get("first_air_date"),
            )
        )
    tv_list.sort(
        key=lambda show: show.popularity,
    )
    return tv_list


def genres(genre_id: int) -> :
    """
    Find Genres
    "genre_ids": [
        53,
        80
    """
    pass
