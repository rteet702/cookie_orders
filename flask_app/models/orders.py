from flask_app.config.mysqlconnection import connectToMySQL


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
        pass