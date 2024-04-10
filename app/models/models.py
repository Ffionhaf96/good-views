from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
    Float,
    Date,
    DateTime,
    Enum,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db.db import engine
from datetime import datetime, timezone

Base = declarative_base()

# Association table for followers/following relationships
followers_table = Table(
    "followers",
    Base.metadata,
    Column("follower_id", ForeignKey("users.id"), primary_key=True),
    Column("followed_id", ForeignKey("users.id"), primary_key=True),
)

# Association table for lists containing movies and TV shows
list_contents_table = Table(
    "list_contents",
    Base.metadata,
    Column("list_id", ForeignKey("lists.id"), primary_key=True),
    Column("content_id", ForeignKey("contents.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    avatar_path = Column(String, default="static/images/avatars/default.svg")
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    lists = relationship("List", backref="user")
    followed = relationship(
        "User",
        secondary=followers_table,
        primaryjoin=(followers_table.c.follower_id == id),
        secondaryjoin=(followers_table.c.followed_id == id),
        backref="followers",
    )


class Content(Base):
    __tablename__ = "contents"
    # id is kept in addition to tmdb_id for instances where users wish to upload there own content descriptor that is not found
    id = Column(Integer, primary_key=True)
    tmdb_id = Column(Integer)
    title = Column(String, nullable=False)
    release_date = Column(Date)
    genres = Column(ARRAY(String))
    description = Column(String)
    content_type = Column(
        Enum("movie", "tv_show", "episode", name="content_type_enum"), nullable=False
    )
    poster_path = Column(String)
    people = relationship("ContentPersonAssociation", back_populates="content")

    # Polymorphic identity configuration
    __mapper_args__ = {
        "polymorphic_identity": "content",
        "polymorphic_on": content_type,
    }


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    tmdb_id = Column(Integer)
    name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    known_for_department = Column(String, nullable=False)
    profile_path = Column(String)

    contents = relationship("ContentPersonAssociation", back_populates="person")


class ContentPersonAssociation(Base):
    __tablename__ = "content_people"
    person_id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
    content_id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
    known_for_department = Column(String, nullable=False)
    character = Column(String, nullable=False)

    person = relationship(Person, back_populates="contents")
    content = relationship(Content, back_populates="people")


class Movie(Content):
    __tablename__ = "movies"
    id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
    duration_minutes = Column(Integer, nullable=False)
    budget = Column(Integer)
    revenue = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": "movie",
    }


class TVShow(Content):
    __tablename__ = "tv_shows"
    id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
    end_date = Column(Date)
    number_of_seasons = Column(Integer)
    seasons = relationship("Season", backref="tv_show")
    __mapper_args__ = {
        "polymorphic_identity": "tv_show",
    }


class Season(Base):
    __tablename__ = "seasons"
    id = Column(Integer, primary_key=True)
    season_number = Column(Integer)
    tv_show_id = Column(Integer, ForeignKey("tv_shows.id"))
    episodes = relationship("Episode", backref="season")


class Episode(Content):
    __tablename__ = "episodes"
    id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
    duration_minutes = Column(Integer, nullable=False)
    episode_number = Column(Integer)
    season_id = Column(Integer, ForeignKey("seasons.id"))

    __mapper_args__ = {
        "polymorphic_identity": "episode",
    }


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content_id = Column(Integer, ForeignKey("contents.id"))
    rating = Column(Float)
    user = relationship("User", backref="ratings")
    content = relationship("Content", backref="ratings")


class List(Base):
    __tablename__ = "lists"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    contents = relationship("Content", secondary=list_contents_table, backref="lists")


Base.metadata.create_all(engine)
