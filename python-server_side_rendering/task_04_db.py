import os
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    """
    Renders the index.html template when the home route is accessed.
    """
    return render_template("index.html")

@app.route("/about")
def about():
    """
    Renders the about.html template when the about route is accessed.
    """
    return render_template("about.html")

@app.route("/contact")
def contact():
    """
    Renders the contact.html template when the contact route is accessed.
    """
    return render_template("contact.html")

@app.route('/items')
def show_items():
    file_path = os.path.join(os.path.dirname(__file__), "items.json")

    with open(file_path, "r") as file:
        data = json.load(file)

    items = data.get("items", [])

    return render_template("items.html", items=items)

def read_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def read_csv(file_path):
    try:
        products = []
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except FileNotFoundError:
        return None

def read_sqlite(db_path, product_id=None):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
        return None

@app.route('/products')
def show_products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    json_path = os.path.join(os.path.dirname(__file__), "products.json")
    csv_path = os.path.join(os.path.dirname(__file__), "products.csv")
    db_path = os.path.join(os.path.dirname(__file__), "products.db")

    if source == "json":
        products = read_json(json_path)
    elif source == "csv":
        products = read_csv(csv_path)
    elif source == "sql":
        products = read_sqlite(db_path, product_id)
    else:
        return render_template("product_display.html", error="Wrong source parameter. Use 'json', 'csv', or 'sql'.")

    if products is None:
        return render_template("product_display.html", error="Error reading data file or database.")

    if product_id and not products:
        return render_template("product_display.html", error="Product not found.")

    return render_template("product_display.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)