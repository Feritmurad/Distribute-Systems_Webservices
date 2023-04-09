from flask import request, make_response
from flask_restful import Resource
import requests
import json
from src.Help_functions import get_movie, api_key, make_standard_json_succes, deleted_movies, check_deleted_movie

class Runtime_movies(Resource):
    def route():
        return '/api/movies/similar_runtime'
    
    def get(self):
        movie = request.args.get('movie')

        # Get movie  genre_ids
        movie_id = get_movie(movie)[0]["id"]
        runtime_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        runtime_params = {
            "api_key": api_key,
            "language": "en-US",
            "append_to_response": "runtimes"
        }
        runtime_response = requests.get(runtime_url, params=runtime_params)

        # Extract runtime from response
        runtime = runtime_response.json()["runtime"]

        # Get movies with 10 minutes difference in runtime
        movies_url = "https://api.themoviedb.org/3/discover/movie"
        movies_params = {
            "api_key": api_key,
            "language": "en-US",
            "runtime.gte": runtime-10,
            "runtime.lte": runtime+10
        }
        response_movies = requests.get(movies_url, params=movies_params)
        movies = response_movies.json()["results"]

        check_deleted_movie(movies)

        # Return standard json
        return make_standard_json_succes(movies)