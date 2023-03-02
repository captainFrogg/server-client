from flask import flash, redirect, render_template
from forms import LoginForm
from database.models.user import User
from flask_login import current_user, login_user, logout_user

from database.models.permissions import Permission


def init_routes(app):

    @app.route('/server-login',  methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated and current_user.can(Permission.ADMIN):
            return redirect('/admin')
        form = LoginForm()
        if form.validate_on_submit():
            user: User = User.query.filter_by(
                username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect('/server-login')
            login_user(user)
            return redirect('/admin')
        return render_template('login.html', title='Sign In', form=form)

    @app.route('/server-logout',  methods=['GET', 'POST'])
    def logout():
        if current_user.is_authenticated:
            logout_user()

        return redirect('/server-login')
