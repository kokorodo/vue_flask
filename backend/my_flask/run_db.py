from app import app,db
from flask_sqlalchemy import  SQLAlchemy
from app.model import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('ok');
