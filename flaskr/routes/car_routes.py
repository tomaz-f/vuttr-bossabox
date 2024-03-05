from flask_restful import Api

from flaskr.resource.resource import Resource


def config_routes(app):
    api = Api()

    api.add_resource(
        Resource, "/", "/<int:id>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
    )

    api.init_app(app)
