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

install_requires = [
    'sqlitedict',
]

setup(
    name='zipgun',
    version='0.2.0',
    description='Postal code library for Python',
    author='Marc Sherry',
    author_email='msherry@gmail.com',
    packages=['zipgun'],
    url='http://github.com/msherry/zipgun',
    tests_require=tests_require,
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
