from data import AirQuality
from collections import defaultdict

def ozone_averages(records):
    city_data = defaultdict(lambda: {"ozone_sum": 0, "ozone_count": 0})
    for record in records:
        if record.ozone is not None:
            city_data[record.city]["ozone_sum"] += record.ozone
            city_data[record.city]["ozone_count"] += 1

    city_averages = {}
    for city, data in city_data.items():
        city_averages[city] = {
            "avg_ozone": data["ozone_sum"] / data["ozone_count"],
            "ozone_count": data["ozone_count"]
        }

    return city_averages

def unhealthy_ozone_days(records):
    city_unhealthy = defaultdict(int)
    for record in records:
        if record.ozone_unhealthy():
            city_unhealthy[record.city] += 1

    return dict(city_unhealthy)


def city_ranks_by_ozone(city_averages):
    cities_with_ozone = [(city, data["avg_ozone"]) for city, data in city_averages.items()]
    cities_with_ozone.sort(key=lambda x: x[1], reverse=True)
    return cities_with_ozone



def ozone_statistics(records):
    ozone_values = [record.ozone for record in records if record.ozone is not None]
    return {
        "min": min(ozone_values),
        "max": max(ozone_values),
        "avg": sum(ozone_values) / len(ozone_values),
        "count": len(ozone_values),
    }


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


def ozone_distribution(records):
    distribution = defaultdict(int)
    for record in records:
        if record.ozone is not None:
            category = record.ozone_level_category()
            distribution[category] += 1
    return dict(distribution)