from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	name = StringField('First and Last Name', 
		validators=[DataRequired(), Length(min=2, max=50)])
	email = StringField("School Email", 
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', 
		validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField("School Email", 
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', 
		validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

