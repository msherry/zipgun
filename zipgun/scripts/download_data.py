#!/usr/bin/env python
"""This script downloads postal data files from GeoNames project website
http://download.geonames.org/export/zip/ and unzips them in current directory

"""
import os
import re
import urllib2
import urlparse
import subprocess


def get_file_list(base_url='http://download.geonames.org/export/zip/'):
    """Get and return postal data files from GeoNames project as
    a (filename, url) iterator

    """
    content = urllib2.urlopen(base_url).read()
    url_pattern = re.compile(r'<a href="([A-Z]{2}\.zip)">')
    for match in url_pattern.finditer(content):
        filename = match.group(1)
        url = urlparse.urljoin(base_url, filename)
        yield (filename, url)


def download_postal_data():
    """Download and unzip all postal data from GeoNames project in current
    directory

    """
    for filename, url in get_file_list():
        print 'Downloading', url, '...'
        content = urllib2.urlopen(url).read()
        with open(filename, 'wb') as zipfile:
            zipfile.write(content)
        subprocess.check_call(['unzip', '-o', filename], shell=False)
        os.remove(filename)

if __name__ == '__main__':
    download_postal_data()
