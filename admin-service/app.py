from flask import Flask
from .v1.apps.v1.models.db import initialize_db
from .v1.routes import initialize_routes
from flask_restful import Api
from .configs import LocalConfig

app = Flask(__name__)
api = Api(app)

app.config.from_object(LocalConfig())
initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run()