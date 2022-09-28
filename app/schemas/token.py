# Import standard library packages

# Import installed packages
# Import app code
from app.schemas.base import BaseSchema
from marshmallow import fields


class TokenSchema(BaseSchema):
    # Own properties
    access_token = fields.Str()
    token_type = fields.Str()
