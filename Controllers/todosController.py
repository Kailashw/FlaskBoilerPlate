import logging
import traceback

from flask import request
from flask_restful import Resource

from Models.todos import todo
from Resources.JSONEncoder import JSONEncoder


class todosController(Resource):
    def get(self):
        try:
            res = []
            if 'id' in request.args:
                cursor = todo.getByid(id)
            else:
                cursor = todo.get()
            for _ in cursor:
                res.append(_)
            return JSONEncoder().encode(res), 200
        except:
            logging.error(traceback.format_exc()), 400
