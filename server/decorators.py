
from functools import wraps
from flask import jsonify, make_response

from flask_jwt_extended import get_jwt_identity

from database.models.user import User


def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            current_user: User = User.query.filter_by(
                username=get_jwt_identity()).first()
            if (not current_user.can(permission=permission)):
                return make_response(jsonify({"msg": "Not allowed"}), 403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator
