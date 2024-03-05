from flask_restful import Api

from flaskr.resource.vuttr_resource import Resource


def config_routes(app):
    api = Api()

    api.add_resource(
        Resource,
        "/tools",
        "/tools/<string:tags>",
        "/tools/<int:id>",
        methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    )

    api.init_app(app)
