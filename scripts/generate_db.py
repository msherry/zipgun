#!/usr/bin/env python

"""
Parses the .txt files from http://download.geonames.org/export/zip/ and turns
them into a sqlite-backed dictionary with sqlitedict
(https://pypi.python.org/pypi/sqlitedict)
"""

import os
import sys

from sqlitedict import SqliteDict

from zipgun import Zipgun, DATA_FILE


def main(data_dir):
    print 'Loading data...'
    zg = Zipgun(data_dir, force_text=True)
    print 'Creating db...'
    persisted = SqliteDict(os.path.join(data_dir, DATA_FILE), autocommit=False)
    print 'Updating data...'
    persisted.update(zg.country_postal_codes)
    print 'Committing data...'
    persisted.commit()

if __name__ == '__main__':
    data_dir = sys.argv[1]
    main(data_dir)
