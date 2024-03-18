from sqlalchemy import Column, Index, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER

from app import db


class User(db.Model):
    __tablename__ = 'user'

    uid = Column(BIGINT, primary_key=True, autoincrement=True, comment='用户id')
    name = Column(String(20), nullable=False, server_default='', comment='名称')
    gender = Column(String(10), nullable=False, server_default='', comment='性别')


    def __repr__(self):
        return '<User : %s %s %s>' % (self.uid, self.name, self.gender)
