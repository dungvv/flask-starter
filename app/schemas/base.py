# Import standard library packages

# Import installed packages
from datetime import date, datetime
from typing import Any, Mapping, Optional

from apiflask import Schema, fields
from marshmallow import ValidationError


class SnowFlakeId(fields.Field):
    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        if value is None:
            return ""
        return str(value)

    def _deserialize(self, value: Any, attr: Optional[str], data: Optional[Mapping[str, Any]], **kwargs):
        try:
            return int(value)
        except ValueError as error:
            raise ValidationError("Id must be digits.") from error


class Dob(fields.Field):
    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        if value is None:
            return None
        else:
            if isinstance(value, date):
                return value.strftime('%Y-%m-%d')
            else:
                return str(value)

    def _deserialize(self, value: Any, attr: Optional[str], data: Optional[Mapping[str, Any]], **kwargs):
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError as error:
            raise ValidationError("Id must be date string.") from error


class CustomDateTime(fields.Field):
    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        if value is None:
            return None
        else:
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%dT%H:%M:%S')
            else:
                return str(value)

    def _deserialize(self, value: Any, attr: Optional[str], data: Optional[Mapping[str, Any]], **kwargs):
        try:
            return datetime.strftime(value, '%Y-%m-%dT%H:%M:%S')
        except ValueError as error:
            raise ValidationError("Id must be date time string.") from error


class BaseSchema(Schema):
    id = SnowFlakeId(dump_only=True)
    pass


class BaseInfoSchema:
    shop_id = SnowFlakeId(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_by = SnowFlakeId(dump_only=True)
    updated_by = SnowFlakeId(dump_only=True)
    is_deleted = fields.Boolean(dump_only=True)


class BaseSchemaSnowIdSecondary(BaseSchema, BaseInfoSchema):
    pass


class BaseSchemaSecondary(Schema, BaseInfoSchema):
    pass
