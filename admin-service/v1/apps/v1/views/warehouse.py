from flask import Response, request, abort
from ..models.warehouse import Warehouse
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

warehouseList_post_fields = {
    "name": fields.String,
    "address": fields.String
}
warehouseList_post_error = {
    "code": fields.String,
    "error raised": fields.String,
    "uri": fields.Url("companiesapi", absolute=True)
}
class WarehouseList(Resource):
    def get(self):
        warehouses = Warehouse.objects().to_json()
        return Response(warehouses, mimetype="application/json", status=200)

    @marshal_with(warehouseList_post_fields, envelope="data")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        body = request.get_json()
        try:
            com = Warehouse(**body).save(force_insert= True)
        except Exception as e:
            return abort(400, marshal({"code": "Warehouse not addded", "error raised": e}, warehouseList_post_error))
        return com, 200

        
