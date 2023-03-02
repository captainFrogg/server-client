from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView

from flask_login import current_user, logout_user
from database.models.user import User
from database.models.role import Role

from flask_admin import AdminIndexView
from flask_admin import expose

from database.models.permissions import Permission


class MyAdminIndexView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.can(Permission.ADMIN)

    # def inaccessible_callback(self, name, **kwargs):
    #     # redirect to login page if user doesn't have access
    #     # logout_user()
    #     # return redirect("/server-login")

    @expose('/')
    def index(self):
        return self.render('admin.html')


class CustomModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.can(Permission.ADMIN)

    # def inaccessible_callback(self, name, **kwargs):
    #     # redirect to login page if user doesn't have access
    #     logout_user()
    #     return redirect("/server-login")


class UserView(CustomModelView):
    column_exclude_list = ['password', ]


def init_admin_view(admin, db):

    admin.add_view(UserView(User, db.session))
    admin.add_view(CustomModelView(Role, db.session))
