from flask import Blueprint

blueprint = Blueprint("errors", __name__)


@blueprint.app_errorhandler(Exception)
def unexpected(e):
    return {
        "code": 500,
        "message": str(e),
        "description": "非預期錯誤",
    }, 500
