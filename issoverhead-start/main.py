import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "kyra342@outlook.com"
MY_PASSWORD = "eppy@kiruri"
MY_LAT = -1.101390  # Your latitude
MY_LONG = 36.798060  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    time.sleep(60)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp-email.outlook.com")
        connection.starttls()
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="theelitecoder7@gmail.com",
                            msg="Subject:LOOKUP\n\nThe iss is above the sky"
                            )
