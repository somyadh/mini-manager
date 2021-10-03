import os
from dotenv import load_dotenv
load_dotenv()

class Configs(object):
    DEBUG = True,
    FLASK_ENV = 'development',
    FLASK_APP = 'app.py'
    TESTING = False

class DockerConfig(Configs):
    MONGODB_SETTINGS = {'host' : os.environ.get('DOCKER_DATABASE_URL') }

class LocalConfig(Configs):
    MONGODB_SETTINGS = {'host' : os.environ.get('LOCAL_DATABASE_URL') }