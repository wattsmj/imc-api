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
Description: A module that contains the IMCInterfaces class to access the iMC API device Ids
'''

from imc._abc import IMCIterable


class IMCInterfaces(IMCIterable):
    'Get method returns all the iMC interfaces that belong to a device'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super().__init__(
            baseurl, username, password, **kwargs)
        self._api = '/imcrs/plat/res/device/{device_id}/interface'
        self._content = IMCIterable._CONTENT_JSON
        self._device_id = None

    @property
    def device_id(self):
        'Getter for device_id'
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        'Setter for device_id'
        try:
            self._device_id = int(value)
        except TypeError:
            raise ValueError("Device ID must be an Integer")

    def get_resource(self):
        '''
        Uses callapi to retrieve the list of devices
        then pulls out IDs and stores them
        '''
        if self._data is None:
            self._data = []
            self._api = self._api.format(
                device_id=self._device_id
            )
            resp = self._callapi()
            interfaces = resp['interface']
            for interface in interfaces:
                self._data.append(int(interface['ifIndex']))
