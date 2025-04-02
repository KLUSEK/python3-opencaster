#! /usr/bin/env python3

import sys
# from distutils.core import setup, Extension
from setuptools import setup, Extension

# from an original source code by Joachim Kaeber (kaeber@gmd.de)
_ext_modules = None

if sys.platform in ['linux2', 'solaris2', 'win32', 'cygwin']:
    _ext_modules = [Extension('dvbobjects.utils._crc32', ['sectioncrc.py.c']), ]

setup(
    name="dvbobjects",
    version="0.1",
    description="Python Package for dvb transport stream data generation (PAT, PMT, NIT, Object Carousel, ...)",
    author="Lorenzo Pallara",
    author_email="l.pallara@avalpa.com",
    url="https://github.com/aventuri/opencaster",

    packages=[
        'dvbobjects',
        'dvbobjects.ATSC',
        'dvbobjects.DSMCC',
        'dvbobjects.DSMCC.BIOP',
        'dvbobjects.DVB',
        'dvbobjects.MHP',
        'dvbobjects.HBBTV',
        'dvbobjects.PSI',
        'dvbobjects.MPEG',
        'dvbobjects.SBTVD',
        'dvbobjects.utils',
    ],
    install_requires=[
        'crcmod',
    ],
    python_requires='>=3.10',
    ext_modules=_ext_modules
)
