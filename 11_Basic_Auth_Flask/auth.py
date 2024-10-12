from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

#1. Read(Retrieve all items)
@auth_bp.route('/profile', methods=['GET'])
#@jwt_required() decorator to enforce authentication and retrieves the current user's identity from the JWT token. 
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    return jsonify({
    'username': user.username,
    'message': f'Welcome to your profile, {user.username}!'
    }), 200


#2. Login Route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    #verify the credentials
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    # Generate JWT token
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200


#Register route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    #insert this data into User model
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists!'}), 400
    
    #add new user to User model
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

    
    
    