from flask_restful import Resource
from ..apps.v1.models.company import Company
# from flask_restful import Resource

# class CompaniesApi(Resource):
#     def get(self):
#         company = Company.objects().to_json()
#         return Response(company, mimetype="application/json", status=200)
#     def post(self):
#         body = request.get_json()
#         com = Company(**body).save()
#         id = com.id
#         return {'id': str(id)}, 200
class seed(Resource):
    def get(self):
        Company.drop_collection()
        try:
            Company.objects.insert([Company( id= 1, name="Syska" ),
                                Company( id= 2, name= "Philips"),
                                ])
        except Exception as e:
            return "seed screwed", 200
        return Company.objects().to_json(), 200
