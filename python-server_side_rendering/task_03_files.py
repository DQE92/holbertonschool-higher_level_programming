import os
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/products')
def show_products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    json_path = os.path.join(os.path.dirname(__file__), "products.json")
    csv_path = os.path.join(os.path.dirname(__file__), "products.csv")

    if source == "json":
        products = read_json(json_path)
    elif source == "csv":
        products = read_csv(csv_path)
    else:
        return render_template("product_display.html", error="Wrong source parameter. Use 'json' or 'csv'.")

    if products is None:
        return render_template("product_display.html", error="Error reading data file.")

    if product_id:
        product = next((p for p in products if p["id"] == product_id), None)
        if product is None:
            return render_template("product_display.html", error="Product not found.")
        products = [product]

    return render_template("product_display.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)