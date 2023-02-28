from flask_admin.contrib.sqla import ModelView
from database.models.user import User
from database.models.role import Role


class UserView(ModelView):
    column_exclude_list = ['password', ]


def init_admin_view(admin, db):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Role, db.session))
