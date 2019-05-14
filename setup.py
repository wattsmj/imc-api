'''
A convience-style partial front-end to the iMC REST API (IMCRS) written in Python 3.
Copyright (C) 2019  Matthew Watts

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Author: wattsmj
Contact: Please raise an issue on www.github.com/wattsmj/imc-api
Description: Package installation file
'''

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
