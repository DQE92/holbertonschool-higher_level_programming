#!/usr/bin/python3
"""
Flask REST API for User Management.

A simple REST API that provides endpoints for managing users, including:
- Creating new users
- Retrieving user information
- Listing all users
- Checking API status

The API uses in-memory storage for demonstration purposes.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for user data
users = {}

@app.route("/")
def home():
    """
    Root endpoint that provides a welcome message.

    Returns:
        str: A welcome message for the API.
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """
    Retrieve a list of all registered usernames.

    Returns:
        Response: A JSON array containing all usernames currently registered in the system.
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    Health check endpoint to verify API functionality.

    Returns:
        str: 'OK' indicating the API is functioning properly.
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """
    Retrieve user information by username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        Response: JSON object containing either:
            - User data if found
            - Error message with 404 status code if user not found
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the system.

    Expects a JSON payload containing user data with at least a 'username' field.
    Example payload:
    {
        "username": "john_doe",
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com"
    }

    Returns:
        Response: JSON object containing either:
            - Success message and user data with 201 status code if user was added
            - Error message with 400 status code if username is missing

    Status Codes:
        201: User successfully created
        400: Username is missing from request
    """
    user_data = request.get_json()
    username = user_data.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run()
