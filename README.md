zipgun
======

A postal code library for Python. Uses data from the [GeoNames project](http://www.geonames.org/).


Usage
-----

* Download all desired data files from the [GeoNames project](http://download.geonames.org/export/zip/) (future versions will have scripts for this)
* (Optional but recommended) Convert these .txt files to a sqlite3-backed db with `scripts/generate_db.py <data_dir>`
* Instantiate a Zipgun instance using the data directory: `zg = Zipgun('data_dir')`
* Query Zipgun instance with a postal code string: 
    ```python
    In [1]: zg.lookup('90210')
    Out[1]:
    {u'city': 'Beverly Hills',
     u'country_code': 'US',
     u'lat': '34.0901',
     u'lon': '-118.4065',
     u'postal_code': '90210',
     u'region': 'CA'}
    
    ```

* Queries default to the United States -- to look up postal codes in other countries (if you've downloaded data files for them), pass the [ISO 3166 alpha 2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2):
    ```python
    In [2]: zg.lookup('4126', 'AR')
    Out[2]:
    {u'city': 'LA CUESTA',
     u'country_code': 'AR',
     u'lat': '-26.0833',
     u'lon': '-65.263',
     u'postal_code': '4126',
     u'region': 'T'}
    ```
