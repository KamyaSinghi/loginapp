from flask import Flask, render_template,request,flash,redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


#from forms import LoginForm, RegisterForm




app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)







