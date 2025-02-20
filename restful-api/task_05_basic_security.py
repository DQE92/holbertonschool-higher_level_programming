#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Should be environment variable in production
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Simulated user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for basic authentication.
    
    Args:
        username (str): The username provided in the request
        password (str): The password provided in the request
        
    Returns:
        str or None: Returns the username if credentials are valid, None otherwise
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Protected route using basic authentication.
    
    Returns:
        tuple: JSON response and HTTP status code
        - Success: ('Basic Auth: Access Granted', 200)
        - Failure: (Authentication error, 401)
    """
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint to obtain JWT token.
    
    Expected JSON payload:
    {
        "username": "string",
        "password": "string"
    }
    
    Returns:
        tuple: JSON response and HTTP status code
        - Success: ({"access_token": "token"}, 200)
        - Failure: ({"error": "message"}, 401)
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401
        
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={'role': users[username]['role']}
        )
        return jsonify({"access_token": access_token}), 200
        
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.
    
    Returns:
        tuple: JSON response and HTTP status code
        - Success: ('JWT Auth: Access Granted', 200)
        - Failure: (Authentication error, 401)
    """
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Protected route for admin users only.
    
    Returns:
        tuple: JSON response and HTTP status code
        - Success: ('Admin Access: Granted', 200)
        - Failure: (Authorization error, 403)
    """
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

# Error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handler for missing JWT token.
    
    Args:
        err: The error message from JWT extended
        
    Returns:
        tuple: JSON response and 401 status code
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handler for invalid JWT token.
    
    Args:
        err: The error message from JWT extended
        
    Returns:
        tuple: JSON response and 401 status code
    """
    return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run()
