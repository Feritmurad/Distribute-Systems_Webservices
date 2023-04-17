import requests
from flask import request, make_response
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
    if len(movie_information) == 0:
        response_content = {
            "status" : "400",
            "data" : None,
            "message" : "Movie not found" 
        }
        response = make_response(response_content)
        response.status_code = 400
        return response
    elif movie_information[0]["title"] in deleted_movies:
        response_content = {
            "status" : "400",
            "data" : None,
            "message" : "Movie has been deleted" 
        }
        response = make_response(response_content)
        response.status_code = 400
        return response

    return movie_information[0]

#Make standard json file for returning
def make_standard_json_succes(list,genres = None, actors = None, runtime = False):
    data = []
    for movie in list:
        movie_dict = {
            "id" : movie["id"],
            "title": movie["title"]            
            }
        if genres is not None:
            movie_dict["genres"] = genres
        if actors is not None:
            movie_dict["actors"] = actors
        if runtime:
            movie_dict["runtime"] = movie["runtime"]
        data.append(movie_dict)     
        
    response_content = {
        "status" : "200",
        "data" : data,
        "message" : "Movies" #### Make a mesage paramater in the function
    }
    
    response = make_response(response_content)
    response.status_code = 200

    return response

def check_deleted_movie(list):
    to_remove = []
    for movie in list:
            for delete_movie in deleted_movies:
                #print(movie["title"],deleted_movies)
                if movie["title"] == delete_movie:
                    to_remove.append(movie)
    for movie in to_remove:
        list.remove(movie)