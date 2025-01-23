from datetime import datetime
from functools import partial
from flask import Flask, request, redirect, url_for, render_template
from utils import generate_itinerary, validate, date_duration, google_map_link, get_location_image
from settings import SECRET_KEY


app = Flask(__name__, template_folder="templates")
app.secret_key = SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/itinerary", methods=["GET", "POST"])
def itinerary():
    if request.method == "POST":
        location = request.form.get("location")

        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        start_date = datetime.strptime(start_date, "%m/%d/%Y").date()
        end_date = datetime.strptime(end_date, "%m/%d/%Y").date()

        if validate(location, start_date, end_date):
            return redirect(url_for("index"))

        num_days = date_duration(start_date, end_date)

        image_url = get_location_image(location)

        itineraries = generate_itinerary(location, num_days)

        app.jinja_env.filters['google_map_link'] = partial(google_map_link, location = location)

        return render_template(
            "itinerary.html",
            location=location,
            image_url=image_url,
            itineraries=itineraries,
        )

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
