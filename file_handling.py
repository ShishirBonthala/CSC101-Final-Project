import csv
import data
from data import AirQuality


def ozone_pm25_air_quality(file):
    pm25_ozone_air_quality = []

    with open(file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for parts in reader:
            date = parts[0]
            city = parts[7]
            pm25 = parts[4]
            ozone = parts[24]

            pm25 = float(pm25) if pm25 != "" else None
            ozone = float(ozone) if ozone != "" else None


            record = AirQuality(city, date, pm25, ozone)
            pm25_ozone_air_quality.append(record)

    return pm25_ozone_air_quality
