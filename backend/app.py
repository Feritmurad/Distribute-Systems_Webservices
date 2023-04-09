from flask import Flask
from flask_restful import Api
from src.Popular_movies import Popular_movies, Popular_movie
from src.Genre_movies import Genre_movies
from src.Runtime_movies import Runtime_movies
from src.Liked_movies import Liked_movies
from src.Actor_movies import Actor_movies

app = Flask(__name__)
api = Api(app)

api.add_resource(Popular_movies, Popular_movies.route())
api.add_resource(Genre_movies, Genre_movies.route())
api.add_resource(Runtime_movies, Runtime_movies.route())
api.add_resource(Popular_movie, Popular_movie.route())
api.add_resource(Liked_movies, Liked_movies.route())
api.add_resource(Actor_movies, Actor_movies.route())

if __name__ == "__main__":
    app.run(host="0.0.0.0")