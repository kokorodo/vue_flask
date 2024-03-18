from flask_wtf import *
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from app.model.User import User

class UserForm(FlaskForm):
    name = StringField(label='Name',
                       validators=[DataRequired('Name is can\'t be empty'),Length(1,20)])
    gender = StringField(label='Gender',
                         validators=[DataRequired('Gender is can\'t be empty'),Length(1,10)])


    def validate_name_exist(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError(u'Name is exists')