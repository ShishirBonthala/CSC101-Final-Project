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

    def test_calculate_pm25_city_averages(self):
        avgs = calculate_pm25_city_averages(self.records)
        self.assertAlmostEqual(avgs['A']['avg_pm25'],15.0)
        self.assertEqual(avgs['A']['pm25_count'],2)
        self.assertAlmostEqual(avgs['B']['avg_pm25'],30.0)
        self.assertEqual(avgs['B']['pm25_count'],1)

    def test_count_unhealthy_pm25_days(self):
        counts = count_unhealthy_pm25_days(self.records)
        self.assertEqual(counts['C'],1)
        self.assertTrue('A' not in counts or counts['A'] == 0)

    def test_rank_cities_by_pm25(self):
        avgs = calculate_pm25_city_averages(self.records)
        ranked = rank_cities_by_pm25(avgs)
        self.assertEqual(ranked[0][0],'C')
        self.assertEqual(ranked[-1][0],'A')

    def test_get_pm25_category(self):
        self.assertEqual(get_pm25_category(8.0),'Good')
        self.assertEqual(get_pm25_category(25.0),'Moderate')
        self.assertEqual(get_pm25_category(50.0),'Unhealthy for Sensitive Groups')
        self.assertEqual(get_pm25_category(70.0),'Unhealthy')

    def test_get_pm25_statistics(self):
        stats = get_pm25_statistics(self.records)
        self.assertEqual(stats['min'],10.0)
        self.assertEqual(stats['max'],60.0)
        self.assertAlmostEqual(stats['avg'],(10.0+20.0+30.0+60.0)/4.0)
        self.assertEqual(stats['count'],4)

    def test_get_pm25_distribution(self):
        dist = get_pm25_distribution(self.records)
        self.assertTrue(dist['Good'] >= 1)
        self.assertTrue(dist['Moderate'] >= 1)
        self.assertTrue(dist['Unhealthy'] >= 1)

    def test_ozone_averages(self):
        avgs = ozone_averages(self.records)
        self.assertAlmostEqual(avgs['A']['avg_ozone'],0.050)
        self.assertEqual(avgs['A']['ozone_count'],2)
        self.assertAlmostEqual(avgs['B']['avg_ozone'],(0.050+0.055)/2)
        self.assertEqual(avgs['B']['ozone_count'],2)

    def test_unhealthy_ozone_days(self):
        counts = unhealthy_ozone_days(self.records)
        self.assertEqual(counts['C'],1)

    def test_city_ranks_by_ozone(self):
        avgs = ozone_averages(self.records)
        ranked = city_ranks_by_ozone(avgs)
        self.assertEqual(ranked[0][0],'C')
        self.assertEqual(ranked[-1][0],'A')

    def test_ozone_statistics(self):
        stats = ozone_statistics(self.records)
        self.assertEqual(stats['min'],0.040)
        self.assertEqual(stats['max'],0.090)
        self.assertAlmostEqual(stats['avg'],(0.040+0.060+0.050+0.055+0.090)/5.0)
        self.assertEqual(stats['count'],5)

    def test_ozone_category(self):
        self.assertEqual(ozone_category(0.040),'Good')
        self.assertEqual(ozone_category(0.060),'Moderate')
        self.assertEqual(ozone_category(0.082),'Unhealthy for Sensitive Groups')
        self.assertEqual(ozone_category(0.090),'Unhealthy')

    def test_ozone_distribution(self):
        dist = ozone_distribution(self.records)
        self.assertTrue(dist['Good'] >= 1)
        self.assertTrue(dist['Moderate'] >= 1)
        self.assertTrue(dist['Unhealthy'] >= 1)

    def test_combined_dictionary(self):
        d = combined_dictionary(self.records)
        self.assertIn('A', d)
        self.assertEqual(len(d['A']['pm25']),2)
        self.assertEqual(len(d['B']['ozone']),2)

    def test_loader_basic(self):
        # Ensure loader returns a non-empty list and objects with expected attributes
        loaded = ozone_pm25_air_quality('ozone_pm25_data.csv')
        self.assertTrue(len(loaded) > 0)
        first = loaded[0]
        self.assertTrue(hasattr(first,'city'))
        self.assertTrue(hasattr(first,'pm25'))
        self.assertTrue(hasattr(first,'ozone'))

if __name__ == '__main__':
    unittest.main()
