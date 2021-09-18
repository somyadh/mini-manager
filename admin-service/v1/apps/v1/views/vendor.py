from flask import Response, request, abort
from ..models.vendor import Vendor
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

vendorList_post_fields = {
    "name": fields.String
}
vendorList_post_error = {
    "code": fields.String,
    "error raised": fields.String,
    "uri": fields.Url("companiesapi", absolute=True)
}
class VendorList(Resource):
    def get(self):
        vendor = Vendor.objects().to_json()
        return Response(vendor, mimetype="application/json", status=200)

    @marshal_with(vendorList_post_fields, envelope="data")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        body = request.get_json()
        print(body)
        try:
            com = Vendor(**body).save(force_insert= True)
        except Exception as e:
           return abort(400, marshal({"code": "Vendor not addded", "error raised": e}, vendorList_post_error))
        # name = com.name
        return com, 200