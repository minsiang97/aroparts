from app import app
from flask import render_template, redirect, url_for, flash, request
from aroparts_web.blueprints.users.views import users_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/", methods=["POST"])
def login():
    data = request.form
    username = data.get("user_username")
    user = User.get_or_none(User.username == username)
    password_to_check = data.get("user_password")

    if user :
        hashed_password = user.password_hash
        result = check_password_hash(hashed_password, password_to_check)
        if result :
            login_user(user)
            flash ("Login successfully", "success")
            return redirect(url_for('admin.index'))
        else :
            flash("Incorrect password", "danger")
            return redirect(url_for('home'))
    
    else :
        flash("Email does not exist", "danger")
        return redirect(url_for('home'))

@app.route("/logout")
def logout():
    logout_user()
    flash("Successfully Logged Out!", "success")
    return redirect(url_for('home'))