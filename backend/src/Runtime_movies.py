from flask import request, make_response
from flask_restful import Resource
from flask import Response
import requests
import json
from src.Help_functions import get_movie, api_key, make_standard_json_succes, deleted_movies, check_deleted_movie

class Runtime_movies(Resource):
    def route():
        return '/api/movies/similar_runtime'
    
    def get(self):
        movie = request.args.get('movie')

        # Get movie  genre_ids
        movie_id = ""
        response = get_movie(movie)
        if isinstance(response, Response):
            return response
        else:
            movie_id = response["id"]


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
            "with_runtime.gte": runtime-10,
            "with_runtime.lte": runtime+10,
        }
        response_movies = requests.get(movies_url, params=movies_params)
        movies = response_movies.json()["results"]
    
        check_deleted_movie(movies)

        """
        for movie in movies:
            movie_details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
            movie_details_params = {
                "api_key": api_key,
                "language": "en-US",
                "append_to_response": "runtimes"
            }
            runtime_response = requests.get(movie_details_url, params=movie_details_params)
            #Extract runtime from response
            runtime = runtime_response.json()["runtime"]
            movie["runtime"] = runtime
        """
            
        # Return standard json
        response = make_standard_json_succes(movies,runtime=False)
        response.status_code = int(200)

        return response
    
    