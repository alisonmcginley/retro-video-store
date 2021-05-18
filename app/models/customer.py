from app.models.rental import Rental
from flask import current_app
from app import db
from .video import Video
from .rental import Rental




class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    postal_code = db.Column(db.Integer)
    phone = db.Column(db.String)
    registered_at = db.Column(db.DateTime)
    videos_checked_out_count = db.Column(db.Integer, nullable=True)
    
    def get_videos(self):
        join_results = db.session.query(Customer, Video, Rental).join(Customer, Customer.id==Rental.customer_id).join (Video, Video.id==Rental.video_id).filter(Customer.id == self.id).all()
        return len(join_results)

    def build_dict(self):
        customer_dict = {
            "id" : self.id,
            "name" : self.name,
            "postal_code" : self.postal_code,
            "phone" : self.phone,
            "registered_at" : self.registered_at,
            "videos_checked_out_count" : self.get_videos()
        } 
        return customer_dict
    
