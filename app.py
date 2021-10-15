from flask import Flask, render_template, request, redirect, url_for
from api_wrapper import get_venues_by_address
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect(url_for("form"))


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return redirect(url_for("form"))
    if request.method == "POST":
        address = request.form.get("Address")
        form_data = get_venues_by_address(address, mock=True)
        return render_template("data.html", form_data=form_data, time=current_time)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
