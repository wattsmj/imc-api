'Package installation file'

from setuptools import setup, find_packages

setup(
    name='imc-api',
    version="0.1.0",
    author='wattsmj',
    description='A convience-style partial front-end to the iMC REST API (IMCRS) written in Python 3.',
    keywords="iMC",
    packages=find_packages(),
    license="LICENSE.txt",
    long_description='README.md',
    install_requires=['requests', 'netaddr']
)
