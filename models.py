"""from app import db

class Company(db.Model):
     __tablename__ = 'company'
     company_id = db.Column(db.Integer, primary_key=True)
     company_name = db.Column(db.String(64), nullable=False)
     scale = db.Column(db.String(30))
     description = db.Column(db.String(512))
     URL = db.Column(db.String(512))
     def __init__(self,company_id,company_name, scale,description,URL):
         self.company_id = company_id
         self.company_name = company_name
         self.scale= scale
         self.description = description
         self.URL=URL
"""
