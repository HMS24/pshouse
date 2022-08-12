from werkzeug.exceptions import HTTPException

from app.api import api
from app.exceptions import ValidationError


@api.app_errorhandler(HTTPException)
def http_error(e):
    return {
        "code": e.code,
        "message": e.name,
        "description": e.description,
    }, e.code


@api.app_errorhandler(ValidationError)
def validation_error(e):
    print("--------------------------- 2")
    return {
        "code": e.status_code,
        "message": "Validation Error",
        "description": "Some errors found below when parsing",
        "errors": e.messages
    }, e.status_code


@api.app_errorhandler(Exception)
def unexpected(e):
    return {
        "code": 500,
        "message": str(e),
        "description": "非預期錯誤",
    }, 500
