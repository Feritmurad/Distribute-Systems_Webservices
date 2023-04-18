from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.Popular_movies import Popular_movies, Popular_movie
from src.Genre_movies import Genre_movies
from src.Runtime_movies import Runtime_movies
from src.Liked_movies import Liked_movies
from src.Actor_movies import Actor_movies
from src.Average_score import Average_Score
from flask_swagger_ui import get_swaggerui_blueprint



SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)


app = Flask(__name__)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
api = Api(app)
CORS(app)

api.add_resource(Popular_movies, Popular_movies.route())
api.add_resource(Genre_movies, Genre_movies.route())
api.add_resource(Runtime_movies, Runtime_movies.route())
api.add_resource(Popular_movie, Popular_movie.route())
api.add_resource(Liked_movies, Liked_movies.route())
api.add_resource(Actor_movies, Actor_movies.route())
api.add_resource(Average_Score,Average_Score.route())



if __name__ == "__main__":
    app.run(host="0.0.0.0")