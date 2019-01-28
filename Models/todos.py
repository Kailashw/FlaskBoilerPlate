from bson.objectid import ObjectId

from Resources import dbConnection


class todos():
    def __init__(self, uids=None):
        self.todos = dbConnection.cur
        self.id = uids

    def get(self):
        return self.todos.find()

    # TODO: need to fetch based on objectId.
    def getByid(self, id):
        key = dict(_id=ObjectId(id))
        return self.todos.find_one(key)


# initialised class so that you don't have to intialize it each time you make a call from controller.
todo = todos()
