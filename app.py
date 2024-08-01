# app.py

from flask import Flask, render_template, redirect, url_for, request
from models import db, Contact, Sale, SupportTicket
from forms import ContactForm, SaleForm, SupportTicketForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SECRET_KEY'] = 'mysecret'

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    contacts = Contact.query.all()
    return render_template('contact_list.html', contacts=contacts)

@app.route('/contact/<int:id>')
def contact_detail(id):
    contact = Contact.query.get_or_404(id)
    return render_template('contact_detail.html', contact=contact)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, email=form.email.data, phone=form.phone.data, company=form.company.data)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts'))
    return render_template('add_contact.html', form=form)

@app.route('/delete_contact/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts'))

@app.route('/sales')
def sales():
    sales = Sale.query.all()
    return render_template('sales_list.html', sales=sales)

@app.route('/add_sale', methods=['GET', 'POST'])
def add_sale():
    form = SaleForm()
    if form.validate_on_submit():
        sale = Sale(contact_id=form.contact_id.data, amount=form.amount.data, date=form.date.data)
        db.session.add(sale)
        db.session.commit()
        return redirect(url_for('sales'))
    return render_template('add_sale.html', form=form)

@app.route('/delete_sale/<int:id>')
def delete_sale(id):
    sale = Sale.query.get_or_404(id)
    db.session.delete(sale)
    db.session.commit()
    return redirect(url_for('sales'))

@app.route('/support_tickets')
def support_tickets():
    tickets = SupportTicket.query.all()
    return render_template('support_tickets.html', tickets=tickets)

@app.route('/add_ticket', methods=['GET', 'POST'])
def add_ticket():
    form = SupportTicketForm()
    if form.validate_on_submit():
        ticket = SupportTicket(contact_id=form.contact_id.data, issue=form.issue.data)
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('support_tickets'))
    return render_template('add_ticket.html', form=form)

@app.route('/delete_ticket/<int:id>')
def delete_ticket(id):
    ticket = SupportTicket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('support_tickets'))

if __name__ == '__main__':
    app.run(debug=True)
