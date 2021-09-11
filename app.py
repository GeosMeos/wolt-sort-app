import requests
import json
import urllib


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
    base_url = "https://restaurant-api.wolt.com/v1/google/places/autocomplete/json?input="
    encoded_address = encode_url(place_address)
    lang = "&language=he"
    type = "&types=geocode"
    request_url = base_url + encoded_address + lang + type
    response = requests.request("GET", request_url).json()
    return response["predictions"][0]["place_id"]


def get_location(place_id) -> str:
    base_url = "https://restaurant-api.wolt.com/v1/google/geocode/json?place_id="
    lang = "&language=he"
    request_url = base_url + place_id + lang
    response = requests.request("GET", request_url).json()
    return response["results"][0]["geometry"]["location"]


def get_venues(coords) -> list:
    base_url = "https://restaurant-api.wolt.com/v1/pages/delivery?"
    lat = str(coords["lat"])
    lon = str(coords["lng"])
    request_url = base_url + "lat=" + lat + "&" + "lon=" + lon
    response = requests.request("GET", request_url).json()
    return response["sections"][0]["items"]


if __name__ == "__main__":
    place_address = "yonitsman 5 tel aviv"
    place_id = get_place_id(place_address)
    location = get_location(place_id)
    venues = get_venues(location)
    for p in venues:
        print(p["title"])