from flask import render_template, redirect
from flask_app import app
from flask_app.models.orders import Order


@app.route('/cookies')
def r_cookies():
    orders = Order.get_all_orders() 
    return render_template('cookies.html', orders=orders)


@app.route('/cookies/new')
def r_cookies_new():
    return render_template('new_order.html')


@app.route('/cookies/placeorder', methods=['POST'])
def f_cookies_new():
    return redirect('/cookies')


@app.route('/cookies/edit/<int:id>')
def r_cookies_edit(id):
    pass