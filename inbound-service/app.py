from flask import Flask
from v1.routes import initialize_routes
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://host.docker.internal:27017/metro-dhruv'
}

initialize_routes(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)