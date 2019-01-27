from flask_restful import Resource

class index(Resource):
    def get(self):
        return {'response': 'successfull'}, 200
