from marshmallow import Schema, fields, validates_schema, ValidationError

Value_CMD = ('filter', 'map', 'unique', 'sort', 'limit')


class ReqestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_cmd(self, values, *args, **kwargs):
        if values['cmd'] not in Value_CMD:
            raise ValidationError("Error CMD")


class AllReqestParams(Schema):
    data = fields.Nested(ReqestParams, many=False)
