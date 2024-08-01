# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    contact = db.relationship('Contact', backref=db.backref('sales', lazy=True))

class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    issue = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default='Open')
    contact = db.relationship('Contact', backref=db.backref('tickets', lazy=True))
