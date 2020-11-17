from datetime import datetime

from marshmallow import Schema, fields, validates_schema, ValidationError

from .utils import (
    len_enough, has_lowercase, has_uppercase, has_numeric
)


class CarResponseSchema(Schema):
    id = fields.Int()
    producer = fields.Str()
    model = fields.Str()
    year = fields.Int(required=True)
    color = fields.Str()
    vin_code = fields.Str(required=True)

    class Meta:
        ordered = True

    @validates_schema
    def validate_year(self, data, **kwargs):
        year = data['year']
        now = datetime.now()
        current_year = int('{:02d}'.format(now.year))
        if not 1980 <= year <= current_year:
            raise ValidationError({'year': f'Year is not in (1980, {current_year}) range'})

    @validates_schema
    def validate_vin_code(self, data, **kwargs):
        vin_code = data['vin_code']
        if not len_enough(vin_code):
            raise ValidationError({'vin_code': 'Vin Code should be exactly 17 characters.'})
        if has_lowercase(vin_code):
            raise ValidationError({'vin_code': 'Vin Code shouldn\'t contain a lowercase letters.'})
        if not has_uppercase(vin_code):
            raise ValidationError({'vin_code': 'Vin Code must contain an uppercase letters.'})
        if not has_numeric(vin_code):
            raise ValidationError({'vin_code': 'Vin Code must contain a digits.'})


class CarRequestSchema(Schema):
    color = fields.Str()


class DeleteCarResponseSchema(Schema):
    message = fields.Str(default="Successfully deleted")
