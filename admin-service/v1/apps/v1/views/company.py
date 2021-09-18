from flask import Response, request, abort
from ..models.company import Company
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

companiesapi_post_fields = {
    "name": fields.String
}
companiesapi_post_error = {
    "code": fields.String,
    "error raised": fields.String,
    "uri": fields.Url("companiesapi", absolute=True)
}
class CompaniesApi(Resource):
    def get(self):
        company = Company.objects().to_json()
        return Response(company, mimetype="application/json", status=200)

    @marshal_with(companiesapi_post_fields, envelope="data")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        body = request.get_json()
        print(body)
        try:
            com = Company(**body).save(force_insert= True)
        except Exception as e:
           return abort(400, marshal({"code": "company not addded", "error raised": e}, companiesapi_post_error))
        return com, 200