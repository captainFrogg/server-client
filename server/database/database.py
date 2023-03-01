from flask_sqlalchemy import SQLAlchemy


class DataBaseManager(object):
    _instance = None
    db: SQLAlchemy

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataBaseManager, cls).__new__(cls)
            cls._instance.db = SQLAlchemy()
        return cls._instance

    def get_db(self):
        return self.db

    def initialize_db(self, app):
        self.app = app
        self.db.init_app(app)
        with self.app.app_context():
            self.db.create_all()
            self.__init_rows()

            # Migrate(self.app, self.db)
            # upgrade()

    def __init_rows(self):

        from .models.user import User
        from .models.role import Role

        roles = Role.query.all()
        users = User.query.all()
        adminRole = None
        if not roles:
            rows = []
            adminRole = Role(name="Admin")
            rows.append(adminRole)
            rows.append(Role(name="User", default=True))
            self.db.session.add_all(rows)
            self.db.session.commit()

        self.init_permissions()

        if adminRole is None:
            adminRole = Role.query.filter_by(name="Admin").first()

        if not users:
            rows = []
            rows.append(
                User(username="admin", email="admin@toto.fr", role_id=adminRole.id))
            self.db.session.add_all(rows)
            self.db.session.commit()

    def init_permissions(self):
        from .models.permissions import Permission
        from .models.role import Role

        roles = {
            'User': [Permission.READ, Permission.WRITE],
            'Admin': [Permission.READ, Permission.WRITE, Permission.ADMIN]
        }

        for role_name in roles.keys():
            role = Role.query.filter_by(name=role_name).first()

            if role is None:
                role = Role(name=role_name, default=role_name == 'User')
            role.reset_permissions()

            for permission in roles[role_name]:
                role.add_permission(permission)

            self.db.session.add(role)
        self.db.session.commit()
