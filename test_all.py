import unittest
from data import AirQuality
from file_handling import ozone_pm25_air_quality
from pm25_functions import (
    calculate_pm25_city_averages,
    count_unhealthy_pm25_days,
    rank_cities_by_pm25,
    get_pm25_category,
    get_pm25_statistics,
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
from dictionary import combined_dictionary

class TestAllFunctions(unittest.TestCase):
    def setUp(self):
        self.records = [
            AirQuality('A','d1',10.0,0.040),
            AirQuality('A','d2',20.0,0.060),
            AirQuality('B','d1',30.0,0.050),
            AirQuality('B','d2',None,0.055),
            AirQuality('C','d1',60.0,0.090),
        ]

    # Core smoke tests: keep minimal but meaningful coverage
    def test_pm25_core(self):
        avgs = calculate_pm25_city_averages(self.records)
        self.assertAlmostEqual(avgs['A']['avg_pm25'],15.0)
        self.assertEqual(avgs['A']['pm25_count'],2)
        counts = count_unhealthy_pm25_days(self.records)
        self.assertEqual(counts['C'],1)
        ranked = rank_cities_by_pm25(avgs)
        self.assertEqual(ranked[0][0],'C')
        self.assertEqual(get_pm25_category(25.0),'Moderate')
        stats = get_pm25_statistics(self.records)
        self.assertEqual(stats['min'],10.0)
        self.assertEqual(stats['max'],60.0)

    def test_ozone_core(self):
        avgs = ozone_averages(self.records)
        self.assertAlmostEqual(avgs['A']['avg_ozone'],0.050)
        self.assertEqual(avgs['A']['ozone_count'],2)
        counts = unhealthy_ozone_days(self.records)
        self.assertEqual(counts['C'],1)
        ranked = city_ranks_by_ozone(avgs)
        self.assertEqual(ranked[0][0],'C')
        self.assertEqual(ozone_category(0.060),'Moderate')
        stats = ozone_statistics(self.records)
        self.assertEqual(stats['min'],0.040)
        self.assertEqual(stats['max'],0.090)

    def test_dict_and_loader(self):
        d = combined_dictionary(self.records)
        self.assertIn('A', d)
        self.assertEqual(len(d['A']['pm25']),2)
        loaded = ozone_pm25_air_quality('ozone_pm25_data.csv')
        self.assertTrue(len(loaded) > 0)
        first = loaded[0]
        self.assertTrue(hasattr(first,'city'))
        self.assertTrue(hasattr(first,'pm25'))
        self.assertTrue(hasattr(first,'ozone'))

if __name__ == '__main__':
    unittest.main()
