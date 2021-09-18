from flask import Response, request, abort
from ..models.wattage import Wattage
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

wattageList_post_fields = {
    "unit": fields.String
}
wattageList_post_error = {
    "code": fields.String,
    "error raised": fields.String,
    "uri": fields.Url("companiesapi", absolute=True)
}
class WattageList(Resource):
    def get(self):
        wattage = Wattage.objects().to_json()
        return Response(wattage, mimetype="application/json", status=200)

    @marshal_with(wattageList_post_fields, envelope="data")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eom', 'unit')
        args = parser.parse_args()
        body = request.get_json()
        print(body)
        try:
            com = Wattage(**body).save(force_insert= True)
        except Exception as e:
           return abort(400, marshal({"code": "Wattage not addded", "error raised": e}, wattageList_post_error))
        # name = com.name
        return com, 200