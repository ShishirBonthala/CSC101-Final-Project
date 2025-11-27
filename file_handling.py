import csv
import data
from data import AirQuality


def pm25_air_quality_data(file):
    pm25_data_air_quality = []

    with open(file, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            parts = line.split(",")

            date = parts[0]
            city = parts[7]
            pm25 = parts[4]

            if pm25 == "":
                pm25 = None
            else:
                pm25 = float(pm25.replace('"', ''))

            ozone = None


            record = AirQuality(city, date, pm25, ozone)
            pm25_data_air_quality.append(record)

    return pm25_data_air_quality



def ozone_air_quality_data(file):
    ozone_data_air_quality = []

    with open(file, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            parts = line.split(",")

            city = parts[6]
            ozone = parts[3]
            date = parts[20]

            if ozone == "":
                ozone = None
            else:
                ozone = float(ozone.replace('"', ''))

            pm25 = None


            record = AirQuality(city, date, pm25, ozone)
            ozone_data_air_quality.append(record)

    return ozone_data_air_quality