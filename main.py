import requests
import smtplib
from datetime import datetime

MY_LAT = 50.993340
MY_LONG = 22.145720

def check_iss():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])


    if abs(MY_LAT - latitude) < 5 and abs(MY_LONG - longitude) < 5:
        return True




parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise = int(sunrise.split("T")[1].split(":")[0])
sunset = int(sunset.split("T")[1].split(":")[0])

time_now = datetime.now().hour

if time_now >= sunset and time_now <= sunrise and check_iss():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user="pythonnzub@gmail.com", password=os.environ("password"))
        connection.sendmail(
            from_addr="pythonnzub@gmail.com", to_addrs='pythonnzub@yahoo.com',
            msg=f"Subject:ISS is coming\n\nLook up!!!!."
        )
else:
    print("Satellite is not close enough to send e-mail")