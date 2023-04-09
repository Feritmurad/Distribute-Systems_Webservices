from flask import request, make_response
from flask_restful import Resource
import requests
import json
from src.Help_functions import liked_movies, deleted_movies

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

        return response_content
            

    
    def post(self):
        #TODO
        movie = request.args.get('movie')

        if movie in liked_movies:
            print("Movie already liked: TO DO")
        else:
            liked_movies.add(movie)
            print("liked", movie)

        return {"liked": "TO DO"}

    def delete(self):
        #TODO
        movie = request.args.get('movie')

        if movie in liked_movies:
            liked_movies.remove(movie)
            print("unliked", movie)

        else:
            print("Movie not liked: TO DO")

        return {"liked": "TO DO"}