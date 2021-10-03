from flask import Response, request, abort
from ..models.sku import SKU
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

skuList_post_fields = {
    "name": fields.String
}
skuList_post_error = {
    "code": fields.String,
    "error raised": fields.String,
    "uri": fields.Url("skulist", absolute=True)
}

class SkuList(Resource):
    def get(self):
        sku = SKU.objects().to_json()
        return Response(sku, mimetype="application/json", status=200)


class Sku(Resource):
    def get(self, name):
        sku = SKU.objects(id=name).to_json()
        return Response(sku, mimetype="application/json", status=200)

    @marshal_with(skuList_post_fields, envelope="data")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        body = request.get_json()
        print(body)
        try:
            com = SKU(**body).save(force_insert= True)
        except Exception as e:
           return abort(400, marshal({"code": "SKU not addded", "error raised": e}, skuList_post_error))
        return com, 200