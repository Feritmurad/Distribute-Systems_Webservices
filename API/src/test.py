from flask import request, make_response
from flask_restful import Resource

class Test(Resource):
    def route():
        return "/test"

    def post(self):
        return make_response("Test is working", 200)
