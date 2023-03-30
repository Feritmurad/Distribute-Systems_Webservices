from flask import request, make_response
from flask_restful import Resource
import requests


class Popular_movies(Resource):
    def route():
        return '/'

    def get(self):

        num_popular_movies = 10 # Need to get from frontend

        # Make a request to the API and get the popular movies
        response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=74f6f8b6965d598eb2d2b2e8b6fcb5d6&language=en-US")
        popular_movies = response.json()["results"]

        # Sort the popular movies by popularity in descending order
        sorted_movies = sorted(popular_movies, key=lambda movie: movie["popularity"], reverse=True)

        response_content = []
        for movie in sorted_movies[:num_popular_movies]:
            movie_dict = {
                "title": movie["title"],
                "popularity": movie["popularity"]}
            response_content.append(movie_dict)

        # Return top 10 
        return response_content
