# coding: utf8
from __future__ import unicode_literals

import unittest
import zipgun

from tests import TestCase

DATA_DIR = 'data'


class TestZipgun(TestCase):

    def setUp(self):
        super(TestZipgun, self).setUp()
        self.zipgun = zipgun.Zipgun(DATA_DIR)

    def test_region(self):
        result = self.zipgun.lookup('94110')
        self.assertEqual(result['region'], 'CA')
        self.assertEqual(result['city'], 'San Francisco')

        result = self.zipgun.lookup('90210')
        self.assertEqual(result['region'], 'CA')
        self.assertEqual(result['city'], 'Beverly Hills')

        result = self.zipgun.lookup('10023')
        self.assertEqual(result['region'], 'NY')
        self.assertEqual(result['city'], 'New York City')

    def test_non_us(self):
        result = self.zipgun.lookup('292-0066', 'JP')
        self.assertEqual(result['city'], 'Shinjuku')

    @unittest.skip("Encoding/decoding doesn't work properly yet")
    def test_unicode(self):
        result = self.zipgun.lookup('452159', 'RU')
        self.assertEqual(result['city'], 'Дмитриевка')
