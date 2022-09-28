# Import standard library packages

# Import installed packages
# Import app code
from app.schemas.base import BaseSchema
from marshmallow import fields


class MsgSchema(BaseSchema):
    # Own properties
    msg = fields.Str()
