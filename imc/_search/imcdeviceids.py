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
Description: A module that contains the IMCdeviceIDs class to access the iMC API device Ids
'''

from imc._abc import IMCIterable


class IMCDeviceIDs(IMCIterable):
    'Get method returns all the iMC devices'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super(IMCDeviceIDs, self).__init__(
            baseurl, username, password, **kwargs)
        self._api = '/imcrs/plat/res/device'
        self._content = IMCIterable._CONTENT_JSON

    def get_resource(self):
        '''
        Uses callapi to retrieve the list of devices
        then pulls out IDs and stores them
        '''
        if self._data is None:
            self._data = []
            resp = self._callapi()
            devices = resp['device']
            for device in devices:
                self._data.append(int(device.get('id')))
