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
Description: A module that contains the base class to access the iMC API
'''

from imc._abc import IMCResource


class IMCNetAsset(IMCResource):
    'Returns the details of a netasset in iMC filtered by advanced query'

    def __init__(self, baseurl, username, password):
        'Initialise the object'

        super(IMCNetAsset, self).__init__(baseurl, username, password)
        self._api = '/imcrs/netasset/asset'
        self._content = IMCResource._CONTENT_JSON
        self._serial = None

    @property
    def serial(self):
        'Getter for serial'
        return self._serial

    @serial.setter
    def serial(self, value):
        'Setter for serial'
        if type(value) is str:
            self._serial = value
        else:
            raise ValueError("Serials must be a string")

    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'

        if self._serial is not None:
            self._options = {'assetSerialNum': self._serial}

    def _get_data(self, item):
        'Returns values from the iMC API response as instance attributes'

        if 'netAsset' not in self._data:
            raise AttributeError(f'No data')

        netasset = self._data['netAsset']

        if type(netasset) is list:
            for chassis in netasset:
                if item in chassis:
                    return chassis[item]

        if type(netasset) is dict:
            if item not in netasset:
                raise AttributeError(f'No attribute {item}')
            return netasset[item]
