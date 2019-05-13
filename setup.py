'Package installation file'

from setuptools import setup, find_packages

setup(
    name='imc-api',
    version="0.1.0",
    author='wattsmj',
    description='iMC API',
    keywords="iMC",
    packages=find_packages(),
    license="LICENSE.txt",
    long_description='README.md',
    install_requires=['requests', 'netaddr']
)
