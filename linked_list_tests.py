import unittest
from linked_list.py import *
class TestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(), None)
    def test_add(self):
        self.assertEqual(add(Pair(5, Pair(10, "mt")), 2, 7.5), Pair(5, Pair(10, Pair(7.5, "mt"))))
        self.assertEqual(add(Pair(5, Pair(10, "mt")), 1, 7.5), Pair(5, Pair(7.5, Pair(10, "mt"))))
        self.assertEqual(add(Pair(5, Pair(10, "mt")), 0, 21), Pair(21, Pair(5, Pair(10, "mt"))))
        self.assertEqual(add(Pair(1234, "mt"), 1, 123), Pair(1234, Pair(123, "mt")))
        self.assertEqual(add(Pair(1234, "mt"), 0, 136), Pair(136, Pair(1234, "mt")))
        self.assertRaises(IndexError, add, Pair(5, "mt"), 2, "nope")
        def test_length(self):
            self.assertEqual(length(Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, "mt")))))), 5)
            self.assertEqual(length(None), 0)
            self.assertEqual(length(Pair("what", "mt")), 1)
