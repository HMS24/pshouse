from flask import Blueprint

blueprint = Blueprint("errors", __name__)


class ValidationError(Exception):
    def __init__(self, status_code, messages):
        self.status_code = status_code
        self.messages = messages


@blueprint.app_errorhandler(ValidationError)
def validation_error(e):
    return {
        "code": e.status_code,
        "message": "Validation Error",
        "description": "Some errors found below when parsing",
        "errors": e.messages
    }, e.status_code


@blueprint.app_errorhandler(Exception)
def unexpected(e):
    return {
        "code": 500,
        "message": str(e),
        "description": "非預期錯誤",
    }, 500
