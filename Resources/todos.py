from flask_restful import Resource
from flask import request


class todos(Resource):
    def get(self):
        if 'id' in request.args:
            return {'response': "You're special."},200
        return {'response': 'GET operation.'}, 200

    def post(self):
        return {'response': 'POST operation.'}, 202
