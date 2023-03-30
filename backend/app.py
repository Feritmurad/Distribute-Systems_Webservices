from flask import Flask
from flask_restful import Api
from src.Popular_movies import Popular_movies

app = Flask(__name__)
api = Api(app)

api.add_resource(Popular_movies, Popular_movies.route())

if __name__ == "__main__":
    app.run(host="0.0.0.0")