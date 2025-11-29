"""
PM2.5 Analysis Functions
Functions for analyzing PM2.5 air quality data.
Author: Drew
"""

from data import AirQuality
from collections import defaultdict


"""
Purpose: This function, when given a list of AirQuality records, returns a dictionary mapping each city to its average PM2.5 level and record count.
Input type: list[AirQuality]
Output type: dict[str, dict]
Example input: [AirQuality("LA", "01/01/25", 15.0, 0.05), AirQuality("LA", "01/02/25", 20.0, 0.06), AirQuality("SF", "01/01/25", 10.0, 0.05)]
Output given the example input: {"LA": {"avg_pm25": 17.5, "pm25_count": 2}, "SF": {"avg_pm25": 10.0, "pm25_count": 1}}
"""
def calculate_pm25_city_averages(records):
    city_data = defaultdict(lambda: {"pm25_sum": 0, "pm25_count": 0})
    
    for record in records:
        if record.pm25 is not None:
            city_data[record.city]["pm25_sum"] += record.pm25
            city_data[record.city]["pm25_count"] += 1
    
    city_averages = {}
    for city, data in city_data.items():
        city_averages[city] = {
            "avg_pm25": data["pm25_sum"] / data["pm25_count"],
            "pm25_count": data["pm25_count"]
        }
    
    return city_averages


"""
Purpose: This function, when given a list of AirQuality records, returns a dictionary mapping each city to the count of days with unhealthy PM2.5 levels (>= 55.5 ug/m3).
Input type: list[AirQuality]
Output type: dict[str, int]
Example input: [AirQuality("LA", "01/01/25", 60.0, 0.07), AirQuality("LA", "01/02/25", 70.0, 0.08), AirQuality("LA", "01/03/25", 20.0, 0.05)]
Output given the example input: {"LA": 2}
"""
def count_unhealthy_pm25_days(records):
    city_unhealthy = defaultdict(int)
    
    for record in records:
        if record.pm_unhealthy():
            city_unhealthy[record.city] += 1
    
    return dict(city_unhealthy)


"""
Purpose: This function, when given a dictionary of city PM2.5 averages, returns a list of tuples with cities ranked from worst (highest) to best (lowest) PM2.5 levels.
Input type: dict[str, dict]
Output type: list[tuple]
Example input: {"LA": {"avg_pm25": 25.0}, "SF": {"avg_pm25": 10.0}, "SD": {"avg_pm25": 15.0}}
Output given the example input: [("LA", 25.0), ("SD", 15.0), ("SF", 10.0)]
"""
def rank_cities_by_pm25(city_averages):
    cities_with_pm25 = [(city, data["avg_pm25"]) for city, data in city_averages.items()]
    cities_with_pm25.sort(key=lambda x: x[1], reverse=True)
    return cities_with_pm25


"""
Purpose: This function, when given a PM2.5 value in ug/m3, returns the EPA health category as a string.
Input type: float
Output type: str
Example input: 25.5
Output given the example input: "Moderate"
Example input: 8.0
Output given the example input: "Good"
"""
def get_pm25_category(value):
    if value <= 12:
        return "Good"
    elif value <= 35.4:
        return "Moderate"
    elif value <= 55.4:
        return "Unhealthy for Sensitive Groups"
    else:
        return "Unhealthy"


"""
Purpose: This function, when given a list of AirQuality records, returns overall PM2.5 statistics including minimum, maximum, and average values across all records.
Input type: list[AirQuality]
Output type: dict[str, float or int]
Example input: [AirQuality("LA", "01/01/25", 10.0, 0.05), AirQuality("LA", "01/02/25", 30.0, 0.06), AirQuality("SF", "01/01/25", 20.0, 0.05)]
Output given the example input: {"min": 10.0, "max": 30.0, "avg": 20.0, "count": 3}
"""
def get_pm25_statistics(records):
    pm25_values = [record.pm25 for record in records if record.pm25 is not None]
    
    return {
        "min": min(pm25_values),
        "max": max(pm25_values),
        "avg": sum(pm25_values) / len(pm25_values),
        "count": len(pm25_values)
    }


"""
Purpose: This function, when given a list of AirQuality records, returns a dictionary showing how many records fall into each EPA health category.
Input type: list[AirQuality]
Output type: dict[str, int]
Example input: [AirQuality("LA", "01/01/25", 8.0, 0.05), AirQuality("LA", "01/02/25", 25.0, 0.06), AirQuality("SF", "01/01/25", 60.0, 0.07)]
Output given the example input: {"Good": 1, "Moderate": 1, "Unhealthy for Sensitive Groups": 0, "Unhealthy": 1}
"""
def get_pm25_distribution(records):
    distribution = defaultdict(int)
    
    for record in records:
        if record.pm25 is not None:
            category = record.pm_level_category()
            distribution[category] += 1
    
    return dict(distribution)
