from flask import Flask, render_template, request, redirect, url_for
from api_wrapper import get_venues_by_address
from datetime import datetime
import logging

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

app = Flask(__name__)


def sort_data(form_data, inputs):
    """
    # Given data and input, sort and return
    """
    try:
        if inputs["options"] == "o1":  # cheapest delivery price
            form_data = sorted(form_data, key=lambda x: x.delivery_price)
        elif inputs["options"] == "o2":  # highest rating score
            form_data = sorted(form_data, key=lambda x: x.score, reverse=True)
        elif inputs["options"] == "o3":  # closest locations
            form_data = sorted(
                ([x for x in form_data if x.price_range > 0]),
                key=lambda x: x.price_range,
            )  # but actually price range for now.
        try:
            if inputs["hide_closed"] == "on":
                form_data = [x for x in form_data if x.status]
        except Exception:
            logging.info("Showing closed venues")
    except Exception:
        logging.info("Error in gathering input")
    finally:
        return form_data


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
    form_data = sort_data(form_data, inputs=request.form)
    return render_template("data.html", form_data=form_data, time=current_time)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
