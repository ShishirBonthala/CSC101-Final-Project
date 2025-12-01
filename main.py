"""Main Program
Purpose: Load daily air quality records (PM2.5 and ozone) for California cities and print basic summaries:
1. Total record count and number of cities.
2. Worst 3 cities by average PM2.5.
3. Worst 3 cities by average Ozone.
4. Top 3 cities by unhealthy PM2.5 day counts.
5. Top 3 cities by unhealthy Ozone day counts.
Input: Optional command line argument with CSV filename (defaults to 'ozone_pm25_data.csv').
Output: Printed lines to the console.
Example: python main.py ozone_pm25_data.csv
"""
import sys
from file_handling import ozone_pm25_air_quality
from pm25_functions import (
    calculate_pm25_city_averages,
    count_unhealthy_pm25_days,
    rank_cities_by_pm25,
    get_pm25_statistics,
    get_pm25_category,
    get_pm25_distribution,
)
from ozone_functions import (
    ozone_averages,
    unhealthy_ozone_days,
    city_ranks_by_ozone,
    ozone_statistics,
    ozone_category,
    ozone_distribution,
)


def main(csv_path):
    try:
        records = ozone_pm25_air_quality(csv_path)
    except FileNotFoundError:
        print("File not found: " + csv_path)
        return

    pm25_stats = get_pm25_statistics(records)
    ozone_stats = ozone_statistics(records)
    pm25_avgs = calculate_pm25_city_averages(records)
    ozone_avgs = ozone_averages(records)

    pm25_ranked = rank_cities_by_pm25(pm25_avgs)
    ozone_ranked = city_ranks_by_ozone(ozone_avgs)
    pm25_top3 = []
    ozone_top3 = []
    for i in range(len(pm25_ranked)):
        if i < 3:
            pm25_top3.append(pm25_ranked[i])
    for i in range(len(ozone_ranked)):
        if i < 3:
            ozone_top3.append(ozone_ranked[i])

    # Cleanest lists removed to keep output minimal

    print("Records: " + str(pm25_stats['count']) + ", Cities: " + str(len(pm25_avgs)))
    print("PM2.5 - min/max/avg: " + str(pm25_stats))
    print("Ozone  - min/max/avg: " + str(ozone_stats))

    print("\nWorst 3 cities by average PM2.5:")
    for city, avg_pm in pm25_top3:
        print(" - " + str(city) + ": " + str(round(avg_pm, 3)) + " ug/m3 (" + str(get_pm25_category(avg_pm)) + ")")

    print("\nWorst 3 cities by average Ozone:")
    for city, avg_o3 in ozone_top3:
        print(" - " + str(city) + ": " + str(round(avg_o3, 3)) + " ppm (" + str(ozone_category(avg_o3)) + ")")

    pm25_unhealthy = count_unhealthy_pm25_days(records)
    ozone_unhealthy = unhealthy_ozone_days(records)
    # Top cities by unhealthy days
    top_pm25_unhealthy = []
    for city in pm25_unhealthy:
        top_pm25_unhealthy.append((city, pm25_unhealthy[city]))
    # Sort descending
    for i in range(len(top_pm25_unhealthy)):
        for j in range(i + 1, len(top_pm25_unhealthy)):
            if top_pm25_unhealthy[i][1] < top_pm25_unhealthy[j][1]:
                top_pm25_unhealthy[i], top_pm25_unhealthy[j] = top_pm25_unhealthy[j], top_pm25_unhealthy[i]
    tmp_pm_unhealthy = []
    for i in range(len(top_pm25_unhealthy)):
        if i < 3:
            tmp_pm_unhealthy.append(top_pm25_unhealthy[i])
    top_pm25_unhealthy = tmp_pm_unhealthy
    
    top_ozone_unhealthy = []
    for city in ozone_unhealthy:
        top_ozone_unhealthy.append((city, ozone_unhealthy[city]))
    # Sort descending
    for i in range(len(top_ozone_unhealthy)):
        for j in range(i + 1, len(top_ozone_unhealthy)):
            if top_ozone_unhealthy[i][1] < top_ozone_unhealthy[j][1]:
                top_ozone_unhealthy[i], top_ozone_unhealthy[j] = top_ozone_unhealthy[j], top_ozone_unhealthy[i]
    tmp_o3_unhealthy = []
    for i in range(len(top_ozone_unhealthy)):
        if i < 3:
            tmp_o3_unhealthy.append(top_ozone_unhealthy[i])
    top_ozone_unhealthy = tmp_o3_unhealthy

    print("\nTop 3 cities by unhealthy PM2.5 days:")
    for city, days in top_pm25_unhealthy:
        print(" - " + str(city) + ": " + str(days) + " days")

    print("\nTop 3 cities by unhealthy Ozone days:")
    for city, days in top_ozone_unhealthy:
        print(" - " + str(city) + ": " + str(days) + " days")

    # Category distributions across all daily records
    # Category distributions removed to keep output short

    # Brief, data-driven insight
    # Insight block removed for minimal output


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "ozone_pm25_data.csv"
    main(csv_path)
