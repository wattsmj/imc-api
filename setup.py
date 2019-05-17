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

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='imc-api',
    version="0.1.0",
    author='wattsmj',
    license="GPL-3.0",
    url="https://github.com/wattsmj/imc-api",
    description='A convience-style partial front-end to the iMC REST API (IMCRS) written in Python 3.',
    long_description=README,
    packages=find_packages(),
    install_requires=['requests', 'netaddr'],
)
