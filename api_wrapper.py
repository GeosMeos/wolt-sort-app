from models.venue import Venue
import requests
import json
import urllib
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG, filemode="w")


def encode_url(address_string) -> str:
    """
    Given an address string, returns the url encoded version of it.
    :param address_string: the address
    :type address_string: str
    :return: url encoded address
    :rtype: str
    """
    encoded_address = urllib.parse.quote_plus(address_string)
    return encoded_address


def get_place_id(place_address) -> str:
    """
    Given an address string, returns the place_id via the api.
    :param place_address: the address
    :type place_address: str
    :return: place_id
    :rtype: str
    """
    base_url = (
        "https://restaurant-api.wolt.com/v1/google/places/autocomplete/json?input="
    )
    encoded_address = encode_url(place_address)
    lang = "&language=he"
    type = "&types=geocode"
    request_url = base_url + encoded_address + lang + type
    response = requests.request("GET", request_url).json()
    return response["predictions"][0]["place_id"]


def get_location(place_id) -> dict:
    """
    Given a place_id string, returns the location(lng,lat) via the api.
    :param place_id: the place_id
    :type place_id: str
    :return: location(lng,lat)
    :rtype: dict
    """
    base_url = "https://restaurant-api.wolt.com/v1/google/geocode/json?place_id="
    lang = "&language=he"
    request_url = base_url + place_id + lang
    response = requests.request("GET", request_url).json()
    return response["results"][0]["geometry"]["location"]


def get_venues(coords) -> dict:
    """
    Given a set of coordinates, returns the venues via the api.
    :param coords: the place_id
    :type coords: str
    :return: venues
    :rtype: dict
    """
    base_url = "https://restaurant-api.wolt.com/v1/pages/delivery?"
    lat = str(coords["lat"])
    lon = str(coords["lng"])
    request_url = base_url + "lat=" + lat + "&" + "lon=" + lon
    response = requests.request("GET", request_url).json()
    return response["sections"][0]["items"]


def build_venues(venues_list):
    """
    ToDo: Docs
    """
    # with open("data.json", "w") as fout:
    #     json.dump(list, fout)
    venueObjList = []
    for p in venues_list:
        try:
            title = p["title"]  # title
            address = p["venue"]["address"]  # address
            delivery_price = p["venue"]["delivery_price"]  # delivery_price
            status = p["venue"]["online"]  # online status
            score = p["venue"]["rating"]["score"]  # rating score
            price_range = p["venue"]["price_range"]  # price_range
        except KeyError as e:
            logging.info(f"KeyError with: {e} | for {title}")
        finally:
            venue = Venue(title, address, delivery_price, status, score, price_range)
            venueObjList.append(venue)
    return venueObjList


def get_venues_by_address(address, mock=False):
    """
    ToDo: Docs
    """
    if not mock:
        place_id = get_place_id(address)
        location = get_location(place_id)
        venues_list = get_venues(location)
        venues = build_venues(venues_list)
    else:
        with open(r"data.json", "r") as read_file:
            mock = json.load(read_file)
            venues = build_venues(mock)
    return venues


"""
if __name__ == "__main__":
    address = "הרצל 45 רמת גן"
    venues = get_venues_by_address(address)
    for v in venues:
        print(v.title)
"""
