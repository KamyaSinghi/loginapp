from flask import Flask, render_template,request,flash,redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.models.user import User

#from forms import LoginForm, RegisterForm




app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager= LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes


