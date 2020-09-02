import io
import os
import re

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ms_cv",
    version="0.1.1",
    url="https://github.com/OpenXbox/ms_cv",
    license='MIT',

    author="OpenXbox",
    author_email="noreply@openxbox.org",

    description="A correlation vector implementation in python",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=['ms_cv'],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'flake8'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
