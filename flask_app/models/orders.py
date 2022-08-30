from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<Order> Object ID: {self.id}'

    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['order_name']) < 2:
            is_valid = False
            flash('Name cannot be empty, and must be at least 2 characters.')
        if len(order['cookie_type']) < 2:
            is_valid = False
            flash('Cookie type cannot be empty, and must be at least 2 characters.')
        if int(order['number_of_boxes']) < 0:
            is_valid = False
            flash('Number of boxes must be one or greater.')
        return is_valid


    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders"
        results = connectToMySQL('cookie-orders').query_db(query)
        orders = []

        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def get_one_order(cls, data):
        query = "SELECT * FROM orders WHERE id=%(id)s;"
        result = connectToMySQL('cookie-orders').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def add_new_order(cls, data):
        query = "INSERT INTO orders (name, cookie_type, number_of_boxes) VALUES (%(name)s, %(cookie_type)s, %(number_of_boxes)s)"
        connectToMySQL('cookie-orders').query_db(query, data)

    @classmethod
    def update_order(cls, data):
        query = "UPDATE orders SET name=%(name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s WHERE id = %(id)s;"
        connectToMySQL('cookie-orders').query_db(query, data)