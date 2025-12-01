"""File Handling Functions
Purpose: Load CSV rows and convert them into AirQuality objects.
Author: Shishir
"""
import csv
from data import AirQuality

"""
Purpose: Read a CSV file and build a list of AirQuality records using PM2.5 and ozone columns.
Input type: file (str path to CSV)
Output type: list[AirQuality]
Example: ozone_pm25_air_quality("ozone_pm25_data.csv") -> [AirQuality(...), ...]
Notes: Skips header row; blank numeric fields become None.
"""
def ozone_pm25_air_quality(file):
    pm25_ozone_air_quality = []
    with open(file, "r") as file_handle:
        reader = csv.reader(file_handle)
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
