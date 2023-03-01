from database.database import DataBaseManager

db = DataBaseManager().get_db()


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship("User", backref="role")

    def __init__(self, name=None, default=False, permissions=None):
        self.name = name
        self.default = default
        if self.permissions is None:
            self.permissions = 0

    def __repr__(self):
        return f'<Role {self.name!r}>'

    def add_permission(self, perm: int):
        if not self.has_permission(perm):
            self.permissions += perm

    def has_permission(self, perm: int):
        return self.permissions & perm == perm

    def remove_permission(self, perm: int):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    @staticmethod
    def get_default():
        return Role.query.filter_by(default=True).first()
