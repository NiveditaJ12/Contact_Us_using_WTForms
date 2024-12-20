from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField 
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField(label='name', validators=[DataRequired()])
    email = EmailField(label='email', validators=[DataRequired()])
    message = TextAreaField(label='message')
    submit = SubmitField(label='Submit')