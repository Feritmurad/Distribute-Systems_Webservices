from flask import request, make_response
from flask import Response
from flask_restful import Resource
import requests
import json
from src.Help_functions import get_movie, make_standard_json_succes, deleted_movies, api_key

class Genre_movies(Resource):
    def route():
        return '/api/movies/similar_genres'
    
    def get(self):
        movie = request.args.get('movie')

        # Get movie  genre_ids
        genre_ids = ""
        response = get_movie(movie)
        if isinstance(response, Response):
            return response
        else:
            genre_ids = response["genre_ids"]


        # make genre_ids a string
        seperator = ","
        genre_ids_str = seperator.join(map(str,genre_ids))

        # Get movies with the same genres
        movies_url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": api_key,
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

        # get the names of the genres using the /genre/movie/list endpoint
        genre_names = []
        for genre_id in genre_ids:
            genre_url = "https://api.themoviedb.org/3/genre/movie/list"
            genre_params = {
                "api_key": api_key,
                "language": "en-US"
            }
            genre_response = requests.get(genre_url, params=genre_params)
            genre_data = genre_response.json()
            for genre in genre_data["genres"]:
                if genre["id"] == genre_id:
                    genre_names.append(genre["name"])

        seperator_space = ", "
        genre_names_str = seperator_space.join(map(str,genre_names))

        # Return all movies
        response = make_standard_json_succes(filtered_movies,genres=genre_names_str)
        response.status_code = int(200)

        return response


