"""
AirQuality class
Purpose: Hold one day's air quality readings (city, date, PM2.5, ozone, and optional AQI) and provide simple helper methods for health checks and categories.
Inputs to constructor: city (str), date (str), pm25 (float or None), ozone (float or None), aqi (int or None)
Example: AirQuality("LA","01/01/25", 12.5, 0.055, 65)
"""
class AirQuality:
    """Simple data holder for one day's readings."""
    def __init__(self, city, date, pm25, ozone, aqi=None):
        """Purpose: Store provided values.
        Inputs: city str, date str, pm25 float/None, ozone float/None, aqi int/None.
        Output: None (object fields are set).
        Example: AirQuality("SF","02/01/25", 10.0, 0.040) creates an instance with those values.
        """
        self.city = city
        self.date = date
        self.pm25 = pm25
        self.ozone = ozone
        self.aqi = aqi

    def pm_unhealthy(self):
        """Purpose: Tell if PM2.5 is in the Unhealthy range.
        Input: uses self.pm25 (float or None).
        Output: bool (True if pm25 >= 55.5).
        Example: AirQuality("X","d", 60.0, 0.040).pm_unhealthy() -> True
        """
        return self.pm25 is not None and self.pm25 >= 55.5

    def pm_level_category(self):
        """Purpose: Return health category name for this PM2.5 value.
        Input: self.pm25.
        Output: str category like "Good" or "Moderate".
        Example: 25.0 -> "Moderate"; None -> "No Data".
        """
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
        """Purpose: Tell if ozone is Unhealthy (>= 0.085 ppm).
        Input: self.ozone.
        Output: bool.
        Example: 0.090 -> True; 0.050 -> False.
        """
        return self.ozone is not None and self.ozone >= 0.085

    def ozone_level_category(self):
        """Purpose: Return ozone health category string.
        Input: self.ozone.
        Output: str category (Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, or No Data).
        Example: 0.060 -> "Moderate".
        """
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
        """Purpose: Tell if AQI is Unhealthy or worse (>= 151).
        Input: self.aqi.
        Output: bool.
        Example: aqi 160 -> True; aqi 100 -> False; None -> False.
        """
        return self.aqi is not None and self.aqi >= 151

    def aqi_category(self):
        """Purpose: Return AQI category string.
        Input: self.aqi (int or None).
        Output: str category.
        Example: 45 -> "Good"; 180 -> "Unhealthy"; None -> "No Data".
        """
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

