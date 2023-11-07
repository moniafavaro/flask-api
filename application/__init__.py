from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qkvbdpcx:CkJR1BfJQpmjrPT3s-PYOTbUbwWN8hxl@trumpet.db.elephantsql.com/qkvbdpcx'
db = SQLAlchemy(app)

from application import routes