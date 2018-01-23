#!/usr/bin/env python
from distutils.core import setup
from pathlib import Path


# Get the long description from the README file
here = Path(__file__).parent
with (here / 'README.md').open(encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Cubic',
    version='1.0.0',
    description='Solve cubic equations.',
    long_description=long_description,
    author='Johan Hidding',
    author_email='j.hidding@esciencecenter.nl',
    packages=['cubic'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering'
    ],

    install_requires=[
        'numpy', 'scipy', 'matplotlib', 'jupyter', 'sdeint'
    ],

    extras_require={
        'develop': [
            'sphinx', 'pytest'
        ]
    }
)
