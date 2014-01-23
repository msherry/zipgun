#!/usr/bin/env python

try:
    import setuptools
except ImportError:
    import distutils.core
    setup = distutils.core.setup
else:
    setup = setuptools.setup

tests_require = [
    'nose >= 1.1.2',
]

setup(
    name='zipgun',
    version='0.1',
    description='Postal code library for Python',
    author='Marc Sherry',
    author_email='msherry@gmail.com',
    py_modules=['zipgun'],
    url='http://github.com/msherry/zipgun',
    tests_require=tests_require,
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
