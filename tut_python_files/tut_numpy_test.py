import by_numpy
import unittest
import numpy as np
import datetime


class NumpyTest(unittest.TestCase):
    def test_count_larger(self):
        self.assertEqual(2, by_numpy.count_larger([1, 2, 3, 4], 2))
        self.assertEqual(1, by_numpy.count_larger([1, 2, 3], 2))
        self.assertEqual(0, by_numpy.count_larger([1, 2], 2))

    def test_sum_square_difference(self):
        self.assertEqual(0, by_numpy.sum_square_difference(0))
        self.assertEqual(0, by_numpy.sum_square_difference(1))
        self.assertEqual(4, by_numpy.sum_square_difference(2))
        self.assertEqual(22, by_numpy.sum_square_difference(3))

    def test_middle_of_elements(self):
        self.assertEqual([1.5, 3], by_numpy.middle_of_elements([1, 2, 4]))

    def test_get_fridays_13(self):
        self.assertEqual(19, len(by_numpy.get_fridays_13()))

        self.assertTrue(datetime.date(2005, 05, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2006, 01, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2006, 10, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2007, 04, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2007, 07, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2008, 06, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2009, 02, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2009, 03, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2009, 11, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2011, 05, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2012, 01, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2012, 04, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2012, 07, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2013, 12, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2014, 06, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2015, 02, 13) in by_numpy.get_fridays_13())
        self.assertTrue(datetime.date(2015, 03, 13) in by_numpy.get_fridays_13())