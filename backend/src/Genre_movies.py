from flask import request, make_response
from flask_restful import Resource
import requests
import json
from src.Help_functions import get_movie, make_standard_json_succes, deleted_movies

class Genre_movies(Resource):
    def route():
        return '/api/movies/similar_genres'
    
    def get(self):
        movie = request.args.get('movie')

        # Get movie  genre_ids
        genre_ids = get_movie(movie)[0]["genre_ids"]

        # make genre_ids a string
        seperator = ","
        genre_ids_str = seperator.join(map(str,genre_ids))

        # Get movies with the same genres
        movies_url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": "74f6f8b6965d598eb2d2b2e8b6fcb5d6",
            "with_genres": genre_ids_str,
        }
        response_movies = requests.get(movies_url, params=params)
        movies = response_movies.json()["results"]

        # Delete movies with more genres

        filtered_movies = []
        for movie in movies:
            if movie["title"] not in deleted_movies: # faster then looping again with check_deleted_movies from help_functions
                if set(movie["genre_ids"]) == set(genre_ids):
                    filtered_movies.append(movie)

        # Return all movies
        return make_standard_json_succes(filtered_movies)


