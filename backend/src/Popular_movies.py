from flask import request, make_response
from flask_restful import Resource
import requests
import json
from src.Help_functions import api_key, make_standard_json_succes, deleted_movies, check_deleted_movie


#https://api.themoviedb.org/3/movie/popular?api_key=74f6f8b6965d598eb2d2b2e8b6fcb5d6&language=en-US&page=2&page_size=50


class Popular_movies(Resource):
    def route():
        return '/api/movies'
    
    def get(self):
        #TODO 
        amount = int(request.args.get('limit',default=20))
        temp_amount = amount + len(deleted_movies)
        
        # Make a request to the API and get the popular movies
        # Predefine variables 
        #response = ""
        popular_movies = []
        page_size = 20
        url = "https://api.themoviedb.org/3/movie/popular"
        pagecounter = 0
        i = 0

        # Loop through pages
        while i < temp_amount:
            pagecounter += 1
    
            params = {
            "api_key": api_key,
            "page": pagecounter,
            "page_size": page_size
            }
            
            response = requests.get(url, params=params)

            data = response.json()
            popular_movies.extend(data["results"])
            i += page_size

        check_deleted_movie(popular_movies)

        # Return all movies
        return make_standard_json_succes(popular_movies[:amount])


class Popular_movie(Resource):
    def route():
        return '/api/movies/<string:movie>'

    def delete(self,movie):
        if movie in deleted_movies:
            print("Movie already deleted: TO DO")
        else:
            deleted_movies.add(movie)
            print("deleted", movie)

        return {"deleted": "TO DO"}

