from flask import Flask, render_template, request, flash, get_flashed_messages, session, redirect, url_for, abort, g
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import datetime
from os import environ

app = Flask(__name__)
class Config(object):
    SECRET_KEY = environ.get("SECRET_KEY") or 'adasdasdasd'

app.permanent_session_lifetime = datetime.timedelta(seconds=10)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dodoDB.db'
db = SQLAlchemy(app)
Bootstrap(app)
