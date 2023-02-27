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
        rows = []

        from .models.user import User
        from .models.role import Role

        roles = Role.query.all()
        users = User.query.all()

        if not roles:
            rows.append(Role(name="Admin"))
            rows.append(Role(name="User"))
        if not users:
            rows.append(User(username="admin", email="admin@toto.fr"))
        self.db.session.add_all(rows)
        self.db.session.commit()
