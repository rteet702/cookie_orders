from flask import render_template, redirect, request
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
    inbound = request.form
    data = {
        'name': inbound['order_name'],
        'cookie_type': inbound['cookie_type'],
        'number_of_boxes': inbound['number_of_boxes']
    }

    if not Order.validate_order(inbound):
        return redirect('/cookies/new')

    Order.add_new_order(data)
    return redirect('/cookies')


@app.route('/cookies/edit/<int:id>')
def r_cookies_edit(id):
    data = {
        'id' : id
    }
    order = Order.get_one_order(data)
    return render_template('edit_order.html', order=order)

@app.route('/cookies/editorder', methods=['POST'])
def f_cookies_edit():
    inbound = request.form
    stored_id = inbound['id']
    data = {
        'id' : stored_id,
        'name' : inbound['order_name'],
        'cookie_type': inbound['cookie_type'],
        'number_of_boxes': inbound['number_of_boxes']
    }
    if not Order.validate_order(inbound):
        return redirect(f'/cookies/edit/{stored_id}')

    Order.update_order(data)
    return redirect('/cookies')