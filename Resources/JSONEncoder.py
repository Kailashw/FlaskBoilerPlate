import json

from bson import ObjectId

'''
    @author : kailas@cloudthing.com
    @description : this function encodes the 'ObjectId' field to string format.
    
'''


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
