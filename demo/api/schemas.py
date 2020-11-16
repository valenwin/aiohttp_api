from marshmallow import Schema, fields


class CarResponseSchema(Schema):
    id = fields.Int()
    producer = fields.Str()
    model = fields.Str()
    year = fields.Int()
    color = fields.Str()
    vin_code = fields.Str()

    class Meta:
        ordered = True