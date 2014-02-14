#!/usr/bin/env python

"""
Parses the .txt files from http://download.geonames.org/export/zip/ and turns
them into a sqlite-backed dictionary with sqlitedict
(https://pypi.python.org/pypi/sqlitedict)
"""

import os
import sys
import time

from sqlitedict import SqliteDict

from zipgun import Zipgun, DATA_FILE


def _persist_v0(file_path, zg):
    print 'Creating db...'
    persisted = SqliteDict(file_path, autocommit=False)
    print 'Updating data...'
    persisted.update(zg.country_postal_codes)
    print 'Committing data...'
    persisted.commit()


def _persist_v1(file_path, zg):
    print 'Creating meta db...'
    zipgun_info = SqliteDict(
        file_path, tablename='zipgun_info', autocommit=False)
    zipgun_info['version'] = 1
    zipgun_info['country_codes'] = zg.country_postal_codes.keys()
    zipgun_info.commit()

    for country_code in zg.country_postal_codes:
        print 'Creating {} db...'.format(country_code)
        country_data = SqliteDict(
            file_path, tablename='zg_{}'.format(country_code),
            autocommit=False)
        country_data.update(zg.country_postal_codes[country_code])
        country_data.commit()
        time.sleep(1.0)                   # Pretty bullshit
        country_data.close()
    zipgun_info.close()


def main(data_dir, version=1):
    file_path = os.path.join(data_dir, DATA_FILE)
    if os.path.exists(file_path):
        print 'Removing old data file...'
        os.remove(file_path)
    print 'Loading text data...'
    zg = Zipgun(data_dir, force_text=True)
    if version == 0:
        _persist_v0(file_path, zg)
    elif version == 1:
        _persist_v1(file_path, zg)

if __name__ == '__main__':
    data_directory = sys.argv[1]
    main(data_directory)
