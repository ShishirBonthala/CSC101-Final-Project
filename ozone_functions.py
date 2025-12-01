"""
Ozone Analysis Functions
Functions for analyzing ground-level ozone data.
Author: Drew
"""

from data import AirQuality

"""
Purpose: When given a list of AirQuality records, return a dictionary mapping each city to its average ozone level and record count.
Input type: list[AirQuality]
Output type: dict[str, dict]
Example input: [AirQuality("LA", "01/01/25", 10.0, 0.060), AirQuality("LA", "01/02/25", 12.0, 0.050), AirQuality("SF", "01/01/25", 8.0, 0.040)]
Output given the example input: {"LA": {"avg_ozone": 0.055, "ozone_count": 2}, "SF": {"avg_ozone": 0.040, "ozone_count": 1}}
"""
def ozone_averages(records):
    city_data = {}
    for record in records:
        if record.ozone is not None:
            if record.city not in city_data:
                city_data[record.city] = {"ozone_sum": 0, "ozone_count": 0}
            city_data[record.city]["ozone_sum"] += record.ozone
            city_data[record.city]["ozone_count"] += 1

    city_averages = {}
    for city in city_data:
        data = city_data[city]
        city_averages[city] = {
            "avg_ozone": data["ozone_sum"] / data["ozone_count"],
            "ozone_count": data["ozone_count"]
        }
    return city_averages


"""
Purpose: When given a list of AirQuality records, return a dictionary mapping each city to how many days had unhealthy ozone (>= 0.086 ppm).
Input type: list[AirQuality]
Output type: dict[str, int]
Example input: [AirQuality("LA", "01/01/25", 10.0, 0.090), AirQuality("LA", "01/02/25", 10.0, 0.050), AirQuality("SF", "01/01/25", 12.0, 0.100)]
Output given the example input: {"LA": 1, "SF": 1}
"""
def unhealthy_ozone_days(records):
    city_unhealthy = {}
    for record in records:
        if record.ozone_unhealthy():
            if record.city not in city_unhealthy:
                city_unhealthy[record.city] = 0
            city_unhealthy[record.city] += 1
    return city_unhealthy


"""
Purpose: When given a dictionary of city ozone averages, return a list of tuples ranked from worst (highest ozone) to best (lowest ozone).
Input type: dict[str, dict]
Output type: list[tuple]
Example input: {"LA": {"avg_ozone": 0.060}, "SF": {"avg_ozone": 0.040}, "SD": {"avg_ozone": 0.050}}
Output given the example input: [("LA", 0.060), ("SD", 0.050), ("SF", 0.040)]
"""
def city_ranks_by_ozone(city_averages):
    cities_with_ozone = []
    for city in city_averages:
        data = city_averages[city]
        cities_with_ozone.append((city, data["avg_ozone"]))

    # Bubble sort descending by average ozone
    for i in range(len(cities_with_ozone)):
        for j in range(i + 1, len(cities_with_ozone)):
            if cities_with_ozone[i][1] < cities_with_ozone[j][1]:
                cities_with_ozone[i], cities_with_ozone[j] = cities_with_ozone[j], cities_with_ozone[i]
    return cities_with_ozone


"""
Purpose: When given a list of AirQuality records, return overall ozone statistics: minimum, maximum, average, and count.
Input type: list[AirQuality]
Output type: dict[str, float or int]
Example input: [AirQuality("LA", "01/01/25", 10.0, 0.040), AirQuality("LA", "01/02/25", 11.0, 0.060), AirQuality("SF", "01/01/25", 9.0, 0.050)]
Output given the example input: {"min": 0.040, "max": 0.060, "avg": 0.050, "count": 3}
"""
def ozone_statistics(records):
    ozone_values = []
    for record in records:
        if record.ozone is not None:
            ozone_values.append(record.ozone)
    return {
        "min": min(ozone_values),
        "max": max(ozone_values),
        "avg": sum(ozone_values) / len(ozone_values),
        "count": len(ozone_values)
    }


"""
Purpose: When given an ozone value in ppm, return its health category string.
Input type: float
Output type: str
Example input: 0.050 -> "Good"
Example input: 0.075 -> "Moderate"
"""
def ozone_category(value):
    if value is None:
        return "No Data"
    elif value <= 0.054:
        return "Good"
    elif value <= 0.070:
        return "Moderate"
    elif value <= 0.085:
        return "Unhealthy for Sensitive Groups"
    else:
        return "Unhealthy"


"""
Purpose: When given a list of AirQuality records, return a dictionary showing how many records fall into each ozone health category.
Input type: list[AirQuality]
Output type: dict[str, int]
Example input: [AirQuality("A", "d", 10.0, 0.040), AirQuality("A", "d2", 11.0, 0.075), AirQuality("B", "d", 8.0, 0.090)]
Output given the example input: {"Good": 1, "Moderate": 1, "Unhealthy": 1}
"""
def ozone_distribution(records):
    distribution = {}
    for record in records:
        if record.ozone is not None:
            category = record.ozone_level_category()
            if category not in distribution:
                distribution[category] = 0
            distribution[category] += 1
    return distribution