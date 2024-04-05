from models.models import Movie, TVShow, Person
from os import getenv
import requests

API_BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = getenv("TMDB_API_KEY")

def movie(title: str):
    pass