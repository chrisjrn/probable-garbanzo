import aqi
import json
import os
import requests

from flask import Flask
from flask.json import jsonify
app = Flask(__name__)

purple_air_feed = os.environ["PURPLE_AIR_URL"]

@app.route('/')
def hello_world():

    feed = requests.get(purple_air_feed).json()

    sensor_a = feedulate(feed["results"][0])

    return sensor_a

def feedulate(results):
    print(results.keys())
    temp_c = (float(results["temp_f"]) - 32) * (5/9)
    return {
        "aqi": str(aqi.to_iaqi(aqi.POLLUTANT_PM25, results["PM2_5Value"], algo=aqi.ALGO_EPA)),
        "pressure": results["pressure"],
        "humidity": results["humidity"],
        "temp_f": results["temp_f"],
        "temp_c": f"{temp_c:.2f}",
    }
