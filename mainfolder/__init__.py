#main.py/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app  = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

####################################
### DATABASE SETUP##################
####################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###################################
#Login Config

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view= 'users.login'


###################################

from mainfolder.core.views import core
from mainfolder.users.views import users
from mainfolder.error_pages.handlers import error_pages
from mainfolder.blog_posts.views import blog_post

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_post)
app.register_blueprint(error_pages)
