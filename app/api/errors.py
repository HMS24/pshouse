from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

from app.api import api
from app.exceptions import ValidationError


def error_response(status_code, message=None):
    payload = {
        "error": HTTP_STATUS_CODES.get(status_code, "Unknown error"),
    }

    if message:
        payload["message"] = message

    response = jsonify(payload)
    response.status_code = status_code

    return response


def bad_request(message):
    return error_response(400, message)


@api.app_errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.messages)
