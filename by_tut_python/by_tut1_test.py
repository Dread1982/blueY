import by_tut1
import unittest
import sys
from StringIO import StringIO


__author__ = 'manuel'


class TutorialsTest(unittest.TestCase):
    def test_print_hello(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            by_tut1.print_hello("world")
            output = out.getvalue().strip()
            self.assertEqual('Hello world', output)
        finally:
            sys.stdout = saved_stdout

    def test_add_vars(self):
        self.assertEqual(7, by_tut1.add_vars(2, 5))
        self.assertEqual(7.5, by_tut1.add_vars(2.5, 5))

        with self.assertRaises(TypeError):
            by_tut1.add_vars(7, "a")

    def test_world_cups(self):
        cups = by_tut1.world_cups()
        self.assertEqual(("Germany", 2006, "Italy"), cups[0])
        self.assertEqual(("South-Africa", 2010, "Spain"), cups[1])
        self.assertEqual(("Brazil", 2014, "Germany"), cups[2])

    def test_add_to_stack(self):
        self.assertEqual([2, 3, 4], by_tut1.add_to_stack([2, 3], 4))

    def test_remove_from_stack(self):
        self.assertEqual([2, 3], by_tut1.remove_from_stack([2, 3, 4]))

    def test_world_cups_by_key(self):
        self.assertEqual(("Germany", 2006, "Italy"), by_tut1.world_cups_by_key(by_tut1.world_cups())["Germany2006"])
        self.assertEqual(("South-Africa", 2010, "Spain"), by_tut1.world_cups_by_key(by_tut1.world_cups())["South-Africa2010"])
        self.assertEqual(("Brazil", 2014, "Germany"), by_tut1.world_cups_by_key(by_tut1.world_cups())["Brazil2014"])

    def test_mutable_immutable(self):
        s = "someString"
        self.assertNotEqual(id(s), id(by_tut1.change_string(s)))

        i = 3
        self.assertNotEqual(id(i), id(by_tut1.change_int(i)))

        l = [1, 2]
        self.assertEqual(id(l), id(by_tut1.change_list(l)))

        d = {"k": "val"}
        self.assertEqual(id(d), id(by_tut1.change_dict(d)))

        with self.assertRaises(AttributeError):
            t = (1, 2)
            by_tut1.a_appended(3, t)

    def test_add_even_numbers_with_for(self):
        self.assertEqual(0, by_tut1.add_even_numbers_with_for(1))
        self.assertEqual(2, by_tut1.add_even_numbers_with_for(2))
        self.assertEqual(2, by_tut1.add_even_numbers_with_for(3))
        self.assertEqual(6, by_tut1.add_even_numbers_with_for(4))
        self.assertEqual(6, by_tut1.add_even_numbers_with_for(5))
        self.assertEqual(12, by_tut1.add_even_numbers_with_for(6))

    def test_add_even_numbers_with_while(self):
        self.assertEqual(0, by_tut1.add_even_numbers_with_while(1))
        self.assertEqual(2, by_tut1.add_even_numbers_with_while(2))
        self.assertEqual(2, by_tut1.add_even_numbers_with_while(3))
        self.assertEqual(6, by_tut1.add_even_numbers_with_while(4))
        self.assertEqual(6, by_tut1.add_even_numbers_with_while(5))
        self.assertEqual(12, by_tut1.add_even_numbers_with_while(6))

    def test_add_even_numbers_elegant(self):
        self.assertEqual(0, by_tut1.add_even_numbers_elegant(1))
        self.assertEqual(2, by_tut1.add_even_numbers_elegant(2))
        self.assertEqual(2, by_tut1.add_even_numbers_elegant(3))
        self.assertEqual(6, by_tut1.add_even_numbers_elegant(4))
        self.assertEqual(6, by_tut1.add_even_numbers_elegant(5))
        self.assertEqual(12, by_tut1.add_even_numbers_elegant(6))

    def test_loop_two_lists(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            by_tut1.loop_two_lists()
            output = out.getvalue().strip()
            self.assertEqual('1 1\n4 8\n9 27\n16 64\n25 125', output)
        finally:
            sys.stdout = saved_stdout

    def test_is_a_bigger_square_in_the_list(self):
        self.assertTrue(by_tut1.is_a_bigger_square_in_the_list(10))

        with self.assertRaises(ValueError):
            by_tut1.is_a_bigger_square_in_the_list(30)

    def test_sum_args_and_kwvalues(self):
        self.assertEqual(35, by_tut1.sum_args_and_kwvalues(3, 2, a=10, b=20))
        self.assertEqual(400, by_tut1.sum_args_and_kwvalues(c=100, d=300))
        self.assertEqual(14, by_tut1.sum_args_and_kwvalues(1, 8, 5))
        self.assertEqual(0, by_tut1.sum_args_and_kwvalues())

    def test_apply_to_all_elements(self):
        a_from_user = 3
        lst = [8, 2, 0, 10]

        def fct(x):
            return x + a_from_user

        self.assertEqual([11, 5, 3, 13], by_tut1.apply_to_all_elements(lst, fct))
        self.assertEqual([11, 5, 3, 13], by_tut1.apply_to_all_elements(lst, lambda x: x + a_from_user))
