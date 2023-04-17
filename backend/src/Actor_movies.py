from flask import request, make_response
from flask_restful import Resource
from flask import Response

import requests
import json
from src.Help_functions import get_movie, make_standard_json_succes, api_key, check_deleted_movie

class Actor_movies(Resource):
    def route():
        return '/api/movies/similar_actors'
    
    def get(self):
        movie = request.args.get('movie')

        # Get movie id
        movie_id = ""
        response = get_movie(movie)
        if isinstance(response, Response):
            return response
        else:
            movie_id = response["id"]

        # Get movie actors

        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
        params = {"api_key": api_key}

        response_actors = requests.get(url, params=params)
        credits = response_actors.json()

        actors_name = [cast["name"] for cast in credits["cast"][:2]]
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
        
        seperator_space = ", "
        actors_names_str = seperator_space.join(map(str,actors_name))
        print(actors_names_str)

        # Return all movies
        response =  make_standard_json_succes(movies,actors=actors_names_str)
        response.status_code = int(200)

        return response