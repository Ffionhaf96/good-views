from models.models import Movie, Person, ContentPersonAssociation, List
from db.db import Session
from tmdb.movie import detail
from tmdb.person import person_detail
from typing import Optional


def populate_from_tmdb(tmdb_id: int) -> Optional[int]:
    """Populate a movie from TMDB into database"""

    # create a new session
    session = Session()

    movie_id = session.query(Movie).filter_by(tmdb_id=tmdb_id).first()
    if movie_id:
        return movie_id.id

    # Get the Movie data
    movie, cast = detail(tmdb_id=tmdb_id)

    # add the movie
    session.add(movie)
    session.commit()

    for cast_member in cast:
        cast_id = cast_member.get("id")
        person = session.query(Person).filter_by(tmdb_id=cast_id).first()
        # if they don't get details from tmdb
        if not person:
            person = person_detail(tmdb_id=cast_id)
            session.add(person)
            session.commit()
        movie_association = ContentPersonAssociation(
            person_id=person.id,
            content_id=movie.id,
            known_for_department=cast_member.get("known_for_department"),
            character=cast_member.get("character"),
        )
        session.add(movie_association)
    session.commit()
    movie_id = session.query(Movie).filter_by(tmdb_id=tmdb_id).first()
    return movie_id.id


def get_by_id(id: int):
    session = Session()
    show = session.get(Movie, id)
    return show


def add_movie_to_list(movie_id: int, list_id: int) -> bool:
    """Add a Movie to a specified list"""
    session = Session()

    movie = session.get(Movie, movie_id)
    content_list = session.get(List, list_id)

    try:
        content_list.append(movie)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't add movie to list - {movie.title} - {e}")
    return None


def remove_movie_from_list(movie_id: int, list_id: int) -> bool:
    """Remove a Movie from a specified list"""
    session = Session()

    movie = session.get(Movie, movie_id)
    content_list = session.get(List, list_id)

    try:
        content_list.remove(movie)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't add movie to list - {movie.title} - {e}")
    return None
