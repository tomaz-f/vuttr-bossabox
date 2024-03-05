from marshmallow import Schema, fields


class Schema(Schema):
    id_car = fields.Int()
    name = fields.Str(required=True)


schema = Schema()
many_schemas = Schema(many=True)
