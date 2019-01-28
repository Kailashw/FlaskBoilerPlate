from Controllers.todosController import todosController
from flaskapp import app, api

api.add_resource(todosController, '/todos')

if __name__ == '__main__':
    app.run(debug=True)
