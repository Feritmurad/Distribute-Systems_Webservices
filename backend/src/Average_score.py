from flask import request, make_response
from flask_restful import Resource
from flask import Response
import base64

import requests
import json
from src.Help_functions import get_movie, make_standard_json_succes, api_key, check_deleted_movie

class Average_Score(Resource):
    def route():
        return '/api/movies/average_score'
    
    def get(self):
        movies = request.args.get('movies')

        movies_list = movies.split(",")
        #movies_list_votes = []
        labels = []
        data = []
        for movie in movies_list:
            response = get_movie(movie)
            if isinstance(response, Response):
                return response
            else:
                labels.append(response["title"])
                data.append(response["vote_average"])
                #movie_dict = {
                    #"title": response["title"],
                    #"vote_average": response["vote_average"]         
                    #}
                #movies_list_votes.append(movie_dict)

        chart_data = {
            "type": 'bar',                                
                "data": {
                    "labels": labels,  
                    "datasets": [{
                        "label": 'Movies',                         
                        "data": data          
                }]
            }
        }

        # Encode the chart data as a JSON string
        chart_data_json = json.dumps(chart_data)

        # Set up the QuickChart API endpoint URL
        quickchart_url = "https://quickchart.io/chart"

        # Make a request to the QuickChart API endpoint with the chart data
        response_chart = requests.get(f"{quickchart_url}?c={chart_data_json}")

        chart_image_base64 = base64.b64encode(response_chart.content).decode('utf-8')


        response_content = {
            "status" : "200",
            "data" : chart_image_base64,
            "message" : "chart"
        }

        response = make_response(response_content)
        response.status_code = 200

        return response