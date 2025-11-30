class AirQuality:
    def __init__(self, city, date, pm25, ozone, aqi=None):
        self.city = city
        self.date = date
        self.pm25 = pm25
        self.ozone = ozone
        self.aqi = aqi

    def pm_unhealthy(self):
        return self.pm25 is not None and self.pm25 >= 55.5

    def pm_level_category(self):
        if self.pm25 is None:
            return "No Data"
        elif self.pm25 <= 12:
            return "Good"
        elif self.pm25 <= 35.4:
            return "Moderate"
        elif self.pm25 <= 55.4:
            return "Unhealthy for Sensitive Groups"
        else:
            return "Unhealthy"

    def ozone_unhealthy(self):
        return self.ozone is not None and self.ozone >= 0.085

    def ozone_level_category(self):
        if self.ozone is None:
            return "No Data"
        elif self.ozone <= 0.054:
            return "Good"
        elif self.ozone <= 0.070:
            return "Moderate"
        elif self.ozone <= 0.085:
            return "Unhealthy for Sensitive Groups"
        else:
            return "Unhealthy"

    def aqi_unhealthy(self):
        return self.aqi is not None and self.aqi >= 151

    def aqi_category(self):
        if self.aqi is None:
            return "No Data"
        if self.aqi <= 50:
            return "Good"
        elif self.aqi <= 100:
            return "Moderate"
        elif self.aqi <= 150:
            return "Unhealthy for Sensitive Groups"
        elif self.aqi <= 200:
            return "Unhealthy"
        elif self.aqi <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

