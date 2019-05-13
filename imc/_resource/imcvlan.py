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


class IMCVlan(IMCResource):
    'Returns the details of a vlan in iMC by device ID'

    def __init__(self, baseurl, username, password):
        'Initialise the object'
        super(IMCVlan, self).__init__(baseurl, username, password)
        self._api = '/imcrs/vlan'
        self._content = IMCResource._CONTENT_JSON
        self._vlan_id = None

    def _get_data(self, item):
        'Returns values from the iMC API response as instance attributes'
        try:
            for vlan in self._data['vlan']:
                if self._vlan_id == int(vlan['vlanId']):
                    return vlan[item]
        except (AttributeError, KeyError):
            raise AttributeError(f'No attribute {item}')

    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'
        self._options.update({'devId': kwargs['device_id'], 'size': 1000})
        self._vlan_id = kwargs['vlan_id']
