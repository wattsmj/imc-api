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
Description: A module that contains the IMCDevicesWithVLAN class to access the iMC API devices with a VLAN
'''

# Dependant IMC imports
from imc._abc import IMCIterable
from . import IMCDeviceIDs

class IMCDevicesWithVLAN(IMCIterable):
    'Get method returns all the iMC devices that have a VLAN'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super(IMCDevicesWithVLAN, self).__init__(baseurl, username, password, **kwargs)
        self._api = '/imcrs/vlan'
        self._content = IMCIterable._CONTENT_JSON
        self._imcdevices = None
        self._vlan_id = None

    @property
    def vlan_id(self):
        'Getter for vlan_id'
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, value):
        'Setter for vlan_id'
        try:
            # Verify the value is a VLAN no.
            vlan_id = int(value)
            if 0 < vlan_id < 4096:
                self._vlan_id = vlan_id
            else:
                raise ValueError("Integer is outside VLAN number range")
        except TypeError:
            raise ValueError("VLAN ID must be an Integer")

    def get_resource(self):
        '''
        Uses callapi to retrieve the list of device IDs
        then pulls out IDs searches for devices with the specified VLAN
        using those IDs
        '''

        # Make sure a VLAN was provided
        # print 'DEBUG: ' + str(self.vlan_id)
        if self.vlan_id is None:
            self._data = []
            return

        if self._data is None:
            self._data = []
            # Make sure we can call the devices iterator
            if self._imcdevices is None:
                self._imcdevices = IMCDeviceIDs(
                    baseurl=self._baseurl,
                    username=self._username,
                    password=self._password,
                    **self._options)

            for deviceid in self._imcdevices:
                self._options.update({'devId': str(deviceid)})
                resp = self._callapi()

                try:
                    for vlan in resp['vlan']:
                        try:
                            if 'vlanId' in vlan:
                                if str(self.vlan_id) in vlan['vlanId']:
                                    self._data.append(deviceid)
                                    break
                        except TypeError:
                            # Didn't get a dictionary back or vlan_id wasn't an integer
                            break
                except (TypeError, KeyError):
                    # Blank response
                    continue