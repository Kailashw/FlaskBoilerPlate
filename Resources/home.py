from flask_restful import Resource


class home(Resource):
    def get(self):
        return {'response': 'successfull in home page'}, 200


class tenant(Resource):
    def get(self):
        return {'response': 'successfull in tenant page'}, 200
