"""
Problem Statement:
    Design an Online Food Delivery System like Swiggy or Zomato.
    Users can browse restaurants, place orders, and track delivery.

"""
from enum import Enum
from typing import List
from uuid import uuid4


class OrderStatus(Enum):
    PLACED = 'placed'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    COMPLETED = 'completed'


class RestaurantStatus(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


class Item:
    def __init__(self, name, price):
        self.id = str(uuid4())
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def update_item(self, item_id, name, price):
        for it in self.items:
            if item_id == it.id:
                it.name = name
                it.price = price


class Order:
    def __init__(self, user, restaurant, items: List[Item]):
        self.id = str(uuid4())
        self.user = user
        self.restaurant = restaurant
        self.items = items
        self.status = OrderStatus.PLACED.value

    def mark_accepted(self):
        self.status = OrderStatus.ACCEPTED.value

    def mark_rejected(self):
        self.status = OrderStatus.REJECTED.value

    def mark_completed(self):
        self.status = OrderStatus.COMPLETED.value

    def calculate_total_amount(self):
        order_total = 0
        for item in self.items:
            order_total += item.price
        return order_total


class Tracker:
    def track_order(self, order):
        print(f"Order:: {order.id} has {order.status} status")


class Restaurant:
    def __init__(self, name, address, mobile, menu):
        self.id = str(uuid4())
        self.name = name
        self.mobile = mobile
        self.address = address
        self.menu = menu
        self.status = RestaurantStatus.CLOSED.value
        self.order_history = []
        self.incoming_orders = []

    def add_item(self, item):
        self.menu.add_item(item)

    def update_item(self, item_id, name, price):
        self.menu.update_item(item_id, name, price)

    def list_order_history(self):
        return self.order_history

    def list_incoming_orders(self):
        return self.incoming_orders

    def accept_order(self, order):
        self.order_history.append(order)
        order.mark_accepted()
        self.incoming_orders.remove(order)

    def reject_order(self, order):
        self.order_history.append(order)
        order.mark_rejected()
        self.incoming_orders.remove(order)

    def mark_restaurant_closed(self):
        self.status = RestaurantStatus.CLOSED.value

    def mark_restaurant_open(self):
        self.status = RestaurantStatus.OPEN.value


class InvoiceGenerator:
    def generate_invoice(self, order):
        print(f"you need to pay {order.calculate_total_amount()} for this order")


class User:
    def __init__(self, mobile, name, address):
        self.id = str(uuid4())
        self.name = name
        self.mobile = mobile
        self.address = address
        self.order_history = []

    def browse_restaurants(self, app):
        return [res for res in app.restaurants if res.status == RestaurantStatus.OPEN.value]

    def place_order(self, restaurant, items: List[Item]):
        if restaurant.status != RestaurantStatus.OPEN.value:
            raise Exception("you can't place order, as the restaurant is closed")
        order = Order(user=self, restaurant=restaurant, items=items)
        self.order_history.append(order)
        restaurant.incoming_orders.append(order)
        return order

    def track_order(self, traker, order):
        return traker.track_order(order)


class Zwiggy:
    def __init__(self):
        self.users = []
        self.restaurants = []

    def add_user(self, user):
        self.users.append(user)

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)
