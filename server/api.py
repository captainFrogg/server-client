# from server.resources.authentication import LoginApi
from resources.authentication import LoginResource, SignUpResource
from resources.user import UserResource


def init_api(api):
    api.add_resource(UserResource, '/user/<user_id>')
    api.add_resource(LoginResource, '/login')
    api.add_resource(SignUpResource, '/sign-up')
