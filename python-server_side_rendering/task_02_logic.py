from flask import Flask, render_template, json
import os

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

if __name__ == "__main__":
    app.run(debug=True)