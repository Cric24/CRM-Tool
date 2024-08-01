# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    company = StringField('Company')
    submit = SubmitField('Add Contact')

class SaleForm(FlaskForm):
    contact_id = StringField('Contact ID', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Sale')

class SupportTicketForm(FlaskForm):
    contact_id = StringField('Contact ID', validators=[DataRequired()])
    issue = TextAreaField('Issue', validators=[DataRequired()])
    submit = SubmitField('Submit Ticket')
