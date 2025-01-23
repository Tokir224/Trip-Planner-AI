import re
import random
import requests
from flask import flash
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from prompt import prompt, llm, parser
from settings import PEXEL_API_KEY


def validate_location(location):
    geolocator = Nominatim(user_agent="trip-planner-ai")
    try:
        location = geolocator.geocode(location)
        if not location:
            flash("Location not found.")
            return True
        return False

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding service error: {e}")


def validate_dates(start_date, end_date):
    if end_date < start_date:
        flash("Arrival date must be after Departure date.")
        return True
    return False


def validate(location, start_date, end_date):
    return validate_location(location) | validate_dates(start_date, end_date)


def date_duration(start_date, end_date):
    date_count = (end_date - start_date).days + 1
    num_days = min(date_count, 5)
    return num_days


def get_location_image(location):
    headers = {
        'Authorization': PEXEL_API_KEY
    }

    per_page = 1
    max_pages = 100
    page = random.randint(1, max_pages)
    query = f"{location} famous places"

    response = requests.get(
        f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}&page={page}", headers=headers)
    data = response.json()
    for photo in data['photos']:
        return photo['src']['original']


def generate_itinerary(location, num_days):
    travel_query = f"Generate a detailed individual days travel itinerary for {location} for {num_days} days."
    chain = prompt | llm | parser
    response = chain.invoke({"query": travel_query})
    return response.itinerary


def google_map_link(text, location):
    pattern1 = re.compile(r'\*\*(.*?)\*\*')
    pattern2 = re.compile(r'\{(.*?)\}')

    def generate_link(match, place_type):
        place = match.group(1)
        return f'<a href="https://www.google.com/maps/search/?api=1&query={place}+{location}" class="{place_type}" target="_blank">{place}</a>'

    text = pattern1.sub(lambda match: generate_link(
        match, "popular-place"), text)
    text = pattern2.sub(lambda match: generate_link(match, "restaurant"), text)

    return text
