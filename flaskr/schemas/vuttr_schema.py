from marshmallow import Schema, fields


class VuttrSchema(Schema):
    id_car = fields.Int()
    title = fields.Str(required=True)
    link = fields.Str(required=True)
    description = fields.Str(required=True)
    tags = fields.Str(required=True)


vuttr_schema = Schema()
vuttr_many_schemas = Schema(many=True)
