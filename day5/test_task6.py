#!/usr/bin/env python
from unittest import TestCase
import task6


class TestPrime(TestCase):
    def setUp(self):
        """Init"""

    def test_invert(self):
        self.assertEqual(task6.invert("one two three"), "eno owt eerht")

    def tearDown(self):
        """Finish"""
