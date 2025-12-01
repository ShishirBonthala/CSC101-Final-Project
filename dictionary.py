"""Dictionary Utilities
Purpose: Build simple combined dictionaries from AirQuality records.
Author: Drew
"""

"""
Purpose: Given a list of AirQuality records, return a dictionary mapping each city to lists of its PM2.5 and ozone values.
Input type: list[AirQuality]
Output type: dict[str, dict]
Example input: [AirQuality("A","d1",10.0,0.040), AirQuality("A","d2",12.0,0.050), AirQuality("B","d1",8.0,0.030)]
Output given example: {"A": {"pm25": [10.0,12.0], "ozone": [0.040,0.050]}, "B": {"pm25": [8.0], "ozone": [0.030]}}
"""
def combined_dictionary(records):
    ozone_pm25_dict = {}
    for record in records:
        city = record.city
        if city not in ozone_pm25_dict:
            ozone_pm25_dict[city] = {"pm25": [], "ozone": []}
        ozone_pm25_dict[city]["pm25"].append(record.pm25)
        ozone_pm25_dict[city]["ozone"].append(record.ozone)
    return ozone_pm25_dict