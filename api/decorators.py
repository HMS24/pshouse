from functools import wraps


def response(schema, status_code=200):
    def decorator(f):
        @wraps(f)
        def _response(*args, **kwargs):
            result = f(*args, **kwargs)

            return schema.jsonify({"data": result}), status_code
        return _response
    return decorator
