from database.database import DataBaseManager

db = DataBaseManager().get_db()


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship("User", backref="role")

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f'<Role {self.name!r}>'
