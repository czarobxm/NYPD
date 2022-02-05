import setuptools
from setuptools import find_packages

setuptools.setup(
    name="pit",
    version="0.1.0",
    license='BSD 2-clause',

    packages=['pit.czytanie_danych.gminy','pit.czytanie_danych.powiaty','pit.czytanie_danych.wojewodztwa','pit.czytanie_danych.testy',
              'pit.analiza_danych', 'pit.analiza_danych.wykres',
              'pit.export'],
    install_requires=["pandas",
                      "numpy",
                      "statistics"]
)
