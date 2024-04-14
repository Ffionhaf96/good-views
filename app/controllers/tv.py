from models.models import (
    TVShow,
    Season,
    Episode,
    Person,
    ContentPersonAssociation,
    List,
)
from db.db import Session
from tmdb.tv import tv_detail, tv_episode_detail
from tmdb.person import person_detail
from typing import Optional


def populate_from_tmdb(tmdb_id: int) -> Optional[int]:
    """Populate a TV Series including seasons and episodes from TMDB"""
    # Create a new session
    session = Session()

    show_id = session.query(TVShow).filter_by(tmdb_id=tmdb_id).first()
    if show_id:
        return show_id.id

    # Get the TV Series data
    series = tv_detail(tmdb_id=tmdb_id)
    # load the genres into an array
    genres = [genre.get("name") for genre in series.get("genres")]

    tv_show = TVShow(
        tmdb_id=tmdb_id,
        title=series.get("name"),
        release_date=series.get("first_air_date"),
        end_date=series.get("end_date"),
        genres=genres,
        description=series.get("overview"),
        content_type="tv_show",
        number_of_seasons=series.get("number_of_seasons"),
        poster_path=series.get("poster_path"),
    )
    # add the TV show
    session.add(tv_show)
    session.commit()

    # get TV Show ID
    show_id = session.query(TVShow).filter_by(tmdb_id=tmdb_id).first()

    # for each person find out if they exist
    # if they do get them
    for cast_member in series.get("credits").get("cast"):
        cast_id = cast_member.get("id")
        person = session.query(Person).filter_by(tmdb_id=cast_id).first()
        # if they don't get details from tmdb
        if not person:
            person = person_detail(tmdb_id=cast_id)
            session.add(person)
            session.commit()
        tv_association = ContentPersonAssociation(
            person_id=person.id,
            content_id=show_id.id,
            known_for_department=cast_member.get("known_for_department"),
            character=cast_member.get("character"),
        )
        session.add(tv_association)
    session.commit()

    for season in series.get("seasons"):
        tv_season = Season(
            season_number=season.get("season_number"), tv_show_id=show_id.id
        )
        session.add(tv_season)
        season_id = (
            session.query(Season)
            .filter_by(tv_show_id=show_id.id, season_number=season.get("season_number"))
            .first()
        )
        for season_episode in range(1, int(season.get("episode_count") + 1)):
            episode = tv_episode_detail(
                tmdb_id=tmdb_id,
                season=season.get("season_number"),
                episode=season_episode,
            )
            episode.season_id = season_id.id
            session.add(episode)
    session.commit()
    show_id = int(show_id.id)
    session.close()

    return show_id


def get_show(id: int):
    session = Session()
    show = session.get(TVShow, id)
    return show


def get_season(show_id: int, season_number: int):
    show = get_show(show_id)
    season = show.season
    print(show.season)
    return season


def get_episode(id: int):
    session = Session()
    show = session.get(TVShow, id)
    return show


def add_episode():
    pass


def add_show_to_list(tv_id: int, list_id: int) -> bool:
    """Add a TVShow to a specified list"""
    session = Session()

    tv_show = session.get(TVShow, tv_id)
    content_list = session.get(List, list_id)

    try:
        content_list.append(tv_show)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't add TV show to list - {tv_show.title} - {e}")
    return None


def remove_show_to_list(tv_id: int, list_id: int) -> bool:
    """Remove a TVShow from the specified list"""
    session = Session()

    tv_show = session.get(TVShow, tv_id)
    content_list = session.get(List, list_id)

    try:
        content_list.remove(tv_show)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Couldn't remove TV show to list - {tv_show.title} - {e}")
    return None
