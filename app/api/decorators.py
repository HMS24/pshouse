from functools import wraps

from webargs.flaskparser import FlaskParser as BaseFlaskParser
from app.exceptions import ValidationError


class FlaskParser(BaseFlaskParser):
    DEFAULT_VALIDATION_STATUS = 400

    def handle_error(
        self, error, req, schema,
        *, error_status_code, error_headers,
    ):
        raise ValidationError(
            error_status_code or self.DEFAULT_VALIDATION_STATUS,
            error.messages,
        )


parser = FlaskParser()
use_args = parser.use_args


def response(schema, status_code=200):
    def decorator(f):
        @wraps(f)
        def _response(*args, **kwargs):
            result = f(*args, **kwargs)

            return schema.jsonify({"result": result}), status_code
        return _response
    return decorator


def querystring(schema, location="querystring", **kwargs):
    def decorator(f):
        return use_args(schema, location=location, **kwargs)(f)

    return decorator
