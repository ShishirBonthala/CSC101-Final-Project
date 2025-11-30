def combined_dictionary(records):
    ozone_pm25_dict = {}

    for record in records:
        city = record.city

        if city not in ozone_pm25_dict:
            ozone_pm25_dict[city] = {"pm25": [], "ozone": []}

        ozone_pm25_dict[city]["pm25"].append(record.pm25)
        ozone_pm25_dict[city]["ozone"].append(record.ozone)


    return ozone_pm25_dict