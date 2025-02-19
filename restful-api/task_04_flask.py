#!/usr/bin/python3
"""
Simple REST API for user management using Flask.

This module implements a basic REST API that allows:
- Retrieving all usernames
- Getting user details by username
- Adding new users
- Checking API status

The data is stored in memory using a dictionary structure.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/")
def home():
    """
    Root endpoint returning a welcome message.

    Returns:
        str: A welcome message for the API.
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_all_usernames():
    """
    Retrieve a list of all registered usernames.

    Returns:
        Response: JSON array containing all usernames in the system.
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    Health check endpoint to verify API functionality.

    Returns:
        str: 'OK' if the API is functioning properly.
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """
    Retrieve detailed information for a specific user.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        Response: JSON object containing user details if found,
                 error message with 404 status code if not found.
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the system.

    Expected JSON payload:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    Returns:
        Response: JSON object containing:
            - Success: message and user data with 201 status code
            - Error: error message with appropriate status code (400 or 409)
    
    Status Codes:
        201: User successfully created
        400: Missing required fields
        409: Username already exists
    """
    data = request.get_json()
    
    if not all(key in data for key in ["username", "name", "age", "city"]):
        return jsonify({"error": "Missing required fields"}), 400
    
    username = data["username"]
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    user_data = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    
    users[username] = user_data
    
    return jsonify({
        "message": "User added successfully",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
