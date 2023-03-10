from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from database.models.user import User
from decorators import permission_required
from database.models.permissions import Permission


class UserResource(Resource):
    @jwt_required()
    @permission_required(Permission.READ)
    def get(self):
        user_id = request.args.get('id', None)
        if (user_id):
            user = User.query.get(user_id)
            return user.to_dict() if user else "No User Found"
        usersResponse = [user.to_dict() for user in User.query.all()]
        return usersResponse if usersResponse else "No Users Found in database"
