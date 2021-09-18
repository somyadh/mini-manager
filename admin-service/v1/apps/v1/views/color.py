from flask import Response, request, abort
from ..models.color import Color
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

colorList_post_fields = {
    "name": fields.String
}
colorList_post_error = {
    "code": fields.String,
    "error raised": fields.String,
    "uri": fields.Url("companiesapi", absolute=True)
}
class ColorList(Resource):
    def get(self):
        color = Color.objects().to_json()
        return Response(color, mimetype="application/json", status=200)

    @marshal_with(colorList_post_fields, envelope="data")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        body = request.get_json()
        try:
            com = Color(**body).save(force_insert= True)
        except Exception as e:
            print(e)
            return abort(400, marshal({"code": "Color not addded", "error raised": e}, colorList_post_error))
        return com, 200
    
    @marshal_with(colorList_post_fields, envelope="data")
    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('old_name', 'new_name')
        args = parser.parse_args()
        body = request.get_json(force=True)
        try:
             a = Color.objects(name= body["old_name"])
             Color.objects(name= body["old_name"]).update(name =body["new_name"])
            #  a.reload()
        except Exception as e:
           return abort(400, marshal({"code": "Color not addded", "error raised": e}, colorList_post_error))
        return {}, 200

        
