from flask import Flask, render_template
from api_wrapper import get_venues_by_address

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
