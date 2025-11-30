from data import AirQuality
from collections import defaultdict

def ozone_averages(records):
    city_data = defaultdict(lambda: {"ozone_sum": 0, "ozone_count": 0})
    for record in records:
        if record.ozone is not None:
            city_data[record.city]["ozone_sum"] += record.pm25
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
    cit
