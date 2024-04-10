from os import getenv
import requests
from typing import Optional
from models.models import Episode

API_BASE_URL = "https://api.themoviedb.org/3/tv/"
API_KEY = getenv("TMDB_API_KEY")


def tv_detail(tmdb_id: int) -> Optional[dict]:
    """
    Retrieves details for a specific TV Show
    """
    series = requests.get(
        f"{API_BASE_URL}{tmdb_id}",
        params={"append_to_response": "credits", "api_key": API_KEY},
        timeout=2,
    )

    if not series.ok:
        print("Didn't get show")
        return None

    return series.json()


def tv_episode_detail(tmdb_id: int, season: int, episode: int) -> Optional[Episode]:
    """
    Retrieves details for a specific TV Show
    """
    tv_episode = requests.get(
        f"{API_BASE_URL}{tmdb_id}/season/{season}/episode/{episode}",
        params={"language": "en-US", "api_key": API_KEY},
        timeout=2,
    )

    if not tv_episode.ok:
        print("Didn't get show")
        return None
    tv_episode = tv_episode.json()
    episode = Episode(
        tmdb_id=tv_episode.get("id"),
        title=tv_episode.get("name"),
        release_date=tv_episode.get("air_date"),
        description=tv_episode.get("overview"),
        duration_minutes=tv_episode.get("runtime"),
        poster_path=tv_episode.get("still_path"),
        episode_number=tv_episode.get("episode_number"),
    )

    return episode
