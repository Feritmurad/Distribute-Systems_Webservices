from flask import request, make_response
from flask_restful import Resource
from flask import Response

import requests
import json
from src.Help_functions import liked_movies, deleted_movies, get_movie

class Liked_movies(Resource):
    def route():
        return '/api/movies/likes'
    

    def get(self):
        
        data = []
        for movie in liked_movies:
            if movie not in deleted_movies: # faster than function
    
                movie_dict = {
                    "title": movie,
                    }
                data.append(movie_dict)     
                
        response_content = {
            "status" : "200",
            "data" : data,
            "message" : None
        }

        response = make_response(response_content)
        response.status_code = 200

        return response
            

    
    def post(self):
        movie = request.args.get('movie')
        response = get_movie(movie)
        if isinstance(response, Response):
            return response
        else:
            movie = response["title"]


        status = ""
        message = ""
    

        
        if movie in liked_movies:
            status = "400"
            message = "Movie is already liked."
        else:
            liked_movies.add(movie)
            status = "200"
            message = "Movie is liked"

        data = [movie]

        response_content = {
            "status" : status,
            "data" : data,
            "message" : message
        }

        response = make_response(response_content)
        response.status_code = int(status)

        return response

    def delete(self):
        movie = request.args.get('movie')
        response = get_movie(movie)
        if isinstance(response, Response):
            return response
        else:
            movie = response["title"]
        
        status = ""
        message = ""

        if movie in liked_movies:
            liked_movies.remove(movie)
            status = "200"
            message = "Movie is unliked"

        else:
            status = "400"
            message = "Movie is not liked."

        data = [movie]

        response_content = {
            "status" : status,
            "data" : data,
            "message" : message
        }

        response = make_response(response_content)
        response.status_code = int(status)

        return response