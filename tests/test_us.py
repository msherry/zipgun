from __future__ import unicode_literals

import zipgun

from tests import TestCase

DATA_DIR = 'data'


class TestUS(TestCase):

    def setUp(self):
        super(TestUS, self).setUp()
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
