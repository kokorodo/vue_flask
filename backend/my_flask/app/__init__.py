from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config


app = Flask(__name__)
app.config["SECRET_KEY"] = "123456"
app.config["WTF_CSRF_CHECK_DEFAULT"] = False
app.config['WTF_CSRF_ENABLED'] = False


app.config.from_object(Config)

# app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
# app.config['SQLALCHEMY_ECHO'] = config.SQLALCHEMY_ECHO

db = SQLAlchemy(app)

# 导入router.py文件，放在db初始化之后
from app import router