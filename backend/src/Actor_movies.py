from flask import request, make_response
from flask_restful import Resource
import requests
import json
from src.Help_functions import get_movie, make_standard_json_succes, api_key, check_deleted_movie

class Actor_movies(Resource):
    def route():
        return '/api/movies/similar_actors'
    
    def get(self):
        movie = request.args.get('movie')

        # Get movie id
        movie_id = get_movie(movie)[0]["id"]

        # Get movie actors

        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
        params = {"api_key": api_key}

        response_actors = requests.get(url, params=params)
        credits = response_actors.json()

        actors = [cast["id"] for cast in credits["cast"][:2]]



        # Get movies with the same genres
        movies_url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": api_key,
            "with_cast": ",".join(str(id) for id in actors),
        }
        response_movies = requests.get(movies_url, params=params)
        movies = response_movies.json()["results"]

        check_deleted_movie(movies)

        # Return all movies
        return make_standard_json_succes(movies)