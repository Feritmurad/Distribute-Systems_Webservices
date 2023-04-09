import requests
import json

api_key = "74f6f8b6965d598eb2d2b2e8b6fcb5d6"

deleted_movies = set()

liked_movies = set()


# Gets all the information of a movie with the given name
def get_movie(movie): 
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": movie
    }
    response  = requests.get(url, params=params)
    movie_information = response.json()["results"]
    return movie_information

#Make standard json file for returning
def make_standard_json_succes(list):
    data = []
    for movie in list:
        movie_dict = {
            "id" : movie["id"],
            "title": movie["title"]            
            }
        data.append(movie_dict)     
        
    response_content = {
        "status" : "200",
        "data" : data,
        "message" : None #### Make a mesage paramater in the function
    }

    return response_content

def check_movie_exists(movie):
    pass
    #TODO


def check_deleted_movie(list):
    for movie in list:
            for delete_movie in deleted_movies:
                if movie["title"] == delete_movie:
                    list.remove(movie)