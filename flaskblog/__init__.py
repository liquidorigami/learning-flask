from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.secrets import token

app = Flask(__name__)
app.config['SECRET_KEY'] = token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes