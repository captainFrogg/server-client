from resources.user_api import UserResource

def init_api(api):
    api.add_resource(UserResource, '/user/<user_id>')