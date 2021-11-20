from flask import Flask, render_template, request, redirect, url_for
from api_wrapper import get_venues_by_address
from datetime import datetime
import logging
from geopy import distance

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

app = Flask(__name__)


def calculate_distance(base_location, venue_location):
    """
    A function to calculate the distance in km between two location coordinates.
    :param base_location: lat,long of the client
    :param venue_location: long,lat of the venue
    :type base_location: dict
    :type venue_location: list
    :return: distance in km
    :rtype: float
    """
    # Switch lat,long coordinates
    venue_location[0], venue_location[1] = venue_location[1], venue_location[0]
    km = distance.distance(base_location.values(), venue_location).km
    return km


def sort_data(form_data, inputs, location):
    """
    Given venue data,inputs and location sort and return data.
    :param form_data: list of Venue objects
    :param inputs: user inputs dict
    :param location: lat, long coordinates of the client
    :type form_data: list
    :type inputs: dict
    :type location: dict
    :return: sorted list of venue objects
    :rtype: list
    """
    try:
        if inputs["options"] == "o0":  # lowest time estimate
            form_data = sorted(form_data, key=lambda x: x.estimate)
        elif inputs["options"] == "o1":  # cheapest delivery price
            form_data = sorted(form_data, key=lambda x: x.delivery_price)
        elif inputs["options"] == "o2":  # highest rating score
            form_data = sorted(form_data, key=lambda x: x.score, reverse=True)
        elif inputs["options"] == "o3":  # cheapest price rating
            form_data = sorted(
                ([x for x in form_data if x.price_range > 0]),
                key=lambda x: x.price_range,
            )
        elif inputs["options"] == "o4":
            form_data = sorted(
                form_data, key=lambda x: calculate_distance(location, x.location)
            )

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
        data = get_venues_by_address(address, mock=False)
        form_data = data[0]
        location = data[1]
    form_data = sort_data(form_data, inputs=request.form, location=location)
    return render_template("data.html", form_data=form_data, time=current_time)


if __name__ == "__main__":
    app.run(port=5000, debug=False)
