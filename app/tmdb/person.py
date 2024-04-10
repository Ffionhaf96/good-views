from models.models import Person
from os import getenv
import requests
from typing import Optional


API_BASE_URL = "https://api.themoviedb.org/3/person/"
API_KEY = getenv("TMDB_API_KEY")


def person_detail(tmdb_id: int) -> Optional[dict]:
    """
    Retrieves details for a specific Person
    """
    person_tmdb = requests.get(
        f"{API_BASE_URL}/{tmdb_id}",
        params={"language": "en-US", "api_key": API_KEY},
        timeout=2,
    )

    if not person_tmdb.ok:
        print("Didn't get show")
        return None
    person_tmdb = person_tmdb.json()
    person = Person(
        tmdb_id=tmdb_id,
        name=person_tmdb.get("name"),
        birthday=person_tmdb.get("birthday"),
        known_for_department=person_tmdb.get("known_for_department"),
        profile_path=person_tmdb.get("profile_path"),
    )

    return person
