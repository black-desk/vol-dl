# coding:utf8
from setuptools import setup

setup(
    name="vol-dl",
    version="0.1",
    packages=["vol_dl"],
    entry_points="""
    [console_scripts]
    vol-dl = vol_dl.vol_dl:main
    """,
    install_requires=["selenium"],
)
