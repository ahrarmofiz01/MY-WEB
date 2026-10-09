from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import  DataRequired, Email,Length
class registrationForm(FlaskForm):
    name=StringField("full name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired(), Length(min=6)])
    submit=SubmitField("submit")