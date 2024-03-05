from flask_restful import Resource
from flask import request
from flaskr.database.connection import db
from flaskr.database.models import VuttrModel
from flaskr.schemas.vuttr_schema import VuttrSchema


class Resource(Resource):
    def get(self):
        if request.args.get("tags"):
            tags = request.args.get("tags")
            tools = VuttrModel.query.filter_by(tags=tags).all()
        else:
            tools = VuttrModel.query.all()
        vuttr_schema = VuttrSchema()
        return vuttr_schema.dump(tools, many=True)

    def post(self):
        try:
            tool = VuttrModel(
                title=request.json["title"],
                link=request.json["link"],
                description=request.json["description"],
                tags=request.json["tags"],
            )
            db.session.add(tool)
            db.session.commit()
            return {"message": "Tool created successfully"}
        except Exception as e:
            return {"message": str(e)}, 400

    def put(self, id_car):
        pass

    def patch(self, id_car):
        pass

    def delete(self, id_car):
        try:
            tool = VuttrModel.query.get(id_car)
            db.session.delete(tool)
            db.session.commit()
            return {"message": "Tool deleted successfully"}
        except Exception as e:
            return {"message": str(e)}, 400
