
from operator import countOf
from flask import current_app
from app import db
from .customer import Customer

def default_available(context):
    return context.get_current_parameters()["total_inventory"]

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime, nullable=True)
    total_inventory = db.Column(db.Integer)
    customers_rented_to = db.relationship('Rental', backref='rental', lazy=True)
    available_inventory = db.Column(db.Integer, default = default_available)
    
    def calculate_inventory(self):
        #calculates remaining inventory
        if self.customers_rented_to:
            self.available_inventory =  self.total_inventory - len([customer for customer in self.customers_rented_to])
        else:
            self.available_inventory = self.total_inventory
        return self.available_inventory

    def build_dict(self):
        #builds video dictionary
        return {
            "id" : self.id,
            "title" : self.title,
            "release_date" : self.release_date,
            "total_inventory" : self.total_inventory,
            "available_inventory" : self.calculate_inventory()
        }
