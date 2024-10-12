#This file contains the User model for the database.
#defines the User model for a Flask application using SQLAlchemy as the ORM (Object-Relational Mapping) and Werkzeug for password hashing and verification.
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
def set_password(self,password):
    self.password = generate_password_hash(password,method='sha256')
    
def check_password(self,password):
    return check_password_hash(self.password, password)



