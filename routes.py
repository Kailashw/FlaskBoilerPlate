from flaskapp import app, api
from Resources.index import index
from Resources.home import home, tenant
from Resources.todos import todos

api.add_resource(index, '/')
api.add_resource(home, '/home')
api.add_resource(tenant, '/tenant')
api.add_resource(todos, '/todos')

if __name__ == '__main__':
    app.run(debug=True)
