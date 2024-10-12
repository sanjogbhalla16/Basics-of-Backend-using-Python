#Main application file 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

# Initialize Flask extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    #This line loads configuration settings for the Flask app from the Config class.
    #The Config class typically contains settings like the database URI, secret keys, and other 
    #application-specific configurations.
    app.config.from_object(Config)
    
    # Initialize extensions
    #This initializes the SQLAlchemy database with the Flask application.
    #This initializes the JWT (JSON Web Token) manager with the Flask app.
    db.init_app(app)
    jwt.init_app(app)
    
    # Import blueprints
    #In Flask, blueprints allow you to organize your routes into reusable, modular components
    from auth import auth_bp
    #By registering the blueprint, all the routes defined in auth_bp (like /login, /register, etc.) will now be part of the Flask app, and you can access them via the appropriate URLs.
    app.register_blueprint(auth_bp)
    
    # Create database
    #creates a context for the app. This is necessary to make certain operations (like database initialization) work outside of a typical request.
    with app.app_context():
        #This line creates all the tables defined in your SQLAlchemy models (like User).
        db.create_all()

    return app

if __name__ == '__main__':
     app = create_app()
     app.run(debug=True)