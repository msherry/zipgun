from __future__ import unicode_literals

from collections import defaultdict
import csv
import glob
import os


class FIELDS(object):
    # iso country code, 2 characters
    COUNTRY_CODE = 0
    # varchar(20)
    POSTAL_CODE = 1
    # City - varchar(180)
    PLACE_NAME = 2
    # 1. order subdivision (state) varchar(100)
    ADMIN_NAME1 = 3
    # 1. order subdivision (state) varchar(20)
    ADMIN_CODE1 = 4
    # 2. order subdivision (county/province) varchar(100)
    ADMIN_NAME2 = 5
    # 2. order subdivision (county/province) varchar(20)
    ADMIN_CODE2 = 6
    # 3. order subdivision (community) varchar(100)
    ADMIN_NAME3 = 7
    # 3. order subdivision (community) varchar(20)
    ADMIN_CODE3 = 8
    # estimated latitude (wgs84)
    LATITUDE = 9
    # estimated longitude (wgs84)
    LONGITUDE = 10
    # accuracy of lat/lng from 1=estimated to 6=centroid
    ACCURACY = 11


class Zipgun(object):

    def __init__(self, data_dir):
        country_postal_codes = defaultdict(lambda: dict())

        fieldnames = sorted([k for k in FIELDS.__dict__ if k.upper() == k],
                            key=lambda x: FIELDS.__dict__[x])
        for filename in glob.glob(os.path.join(data_dir, '*')):
            with open(filename) as f:
                reader = csv.DictReader(f, fieldnames=fieldnames,
                                        delimiter=str('\t'))
                for line in reader:
                    print line
                    postal_codes = (
                        country_postal_codes[line['COUNTRY_CODE']])
                    postal_code = line['POSTAL_CODE']
                    data = {
                        'region': line['ADMIN_CODE1'],
                        'city': line['PLACE_NAME'],
                        'lat': line['LATITUDE'],
                        'lon': line['LONGITUDE'],
                    }
                    if postal_code in postal_codes:
                        postal_codes[postal_code].update(data)
                    else:
                        postal_codes[postal_code] = data
        self.country_postal_codes = dict(country_postal_codes)

    def lookup(self, postal_code, country_code='US'):
        postal_codes = self.country_postal_codes[country_code]
        return postal_codes.get(postal_code, {})
