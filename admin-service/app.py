from flask import Flask
from v1.apps.v1.models.db import initialize_db
from v1.routes import initialize_routes
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://host.docker.internal:27017/metro-dhruv'
}

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run()