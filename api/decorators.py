from functools import wraps

from webargs.flaskparser import use_args


def response(schema, status_code=200):
    def decorator(f):
        @wraps(f)
        def _response(*args, **kwargs):
            result = f(*args, **kwargs)

            return schema.jsonify({"data": result}), status_code
        return _response
    return decorator

def query_string(schema, location="query", **kwargs):
    def decorator(f):
        return use_args(schema, location=location, **kwargs)(f)

    return decorator
