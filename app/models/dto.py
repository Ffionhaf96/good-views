from dataclasses import dataclass
from typing import Optional


@dataclass
class Content:
    tmdb_id: int
    overview: str
    popularity: float
    poster_path: Optional[str]


@dataclass
class Movie(Content):
    title: str
    release_date: str


@dataclass
class TVShow(Content):
    name: str
    first_air_date: str


# @dataclass
# class Episode(Content):


# @dataclass
# class Person():
