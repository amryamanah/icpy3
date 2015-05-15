__author__ = 'amryf'

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="icpy3",
    version="0.0.0",
    description="A simple The imaging Source python binding library",
    long_description=long_description,
    url="",
    author="Amry Amanah",
    author_email="amryfitra@gmail.com",
    license="MIT",
    packages=find_packages(),
    package_data={
        "":['*.txt', '*.rst', '*.dll']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ]

)