from flask import Response
from flask_restful import Resource, fields

class Welcome(Resource):
    def get(self):
        return Response("Welcome to your Mini Manager's Inbound Service", status=200)


        
