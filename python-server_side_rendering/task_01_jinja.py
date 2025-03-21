from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
