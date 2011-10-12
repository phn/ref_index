#!/usr/bin/env python

from distutils.core import setup

import ref_index

version = ref_index.__version__

description = """\
Refractive index of air, and vacuum-air wave length conversion."""

long_description = open("README.rst").read()

setup(
    name="ref_index",
    version=version,
    description=description,
    long_description=long_description,
    license='BSD',
    author="Prasanth Nair",
    author_email="prasanthhn@gmail.com",
    url='http://github.com/phn/ref_index',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python',
        ],
    py_modules=["ref_index"]
    )
