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
Description: A module that contains an iMC object resource factory
'''

from imc._resource import (
    IMCDevice,
    IMCVlan,
    IMCInterface,
    IMCNetAsset
)


class IMCResourceFactory(object):
    '''
    A factory class that returns IMC objects that represent specific iMC resources
    '''

    TYPE_DEVICE = 'DEVICE'
    TYPE_VLAN = 'VLAN'
    TYPE_INTERFACE = 'INTERFACE'
    TYPE_NETASSET = 'NETASSET'

    def __init__(self, baseurl, username, password):
        'Initialise the object'
        self._baseurl = baseurl
        self._username = username
        self._password = password

    def _create_instance(self, class_type, **kwargs):
        '''
        Returns an instance of the given class type under IMCResource
        '''
        # Create an instance of the type
        instance = class_type(
            baseurl=self._baseurl,
            username=self._username,
            password=self._password
        )
        instance.get_resource(**kwargs)
        # Return the instance
        return instance

    def _get_device(self, **kwargs):
        try:
            return self._create_instance(IMCDevice, **kwargs)
        except (ValueError, KeyError):
            raise ValueError("Missing device id")

    def _get_vlan(self, **kwargs):
        try:
            return self._create_instance(IMCVlan, **kwargs)
        except (ValueError, KeyError):
            raise ValueError("Missing device id")

    def _get_interface(self, **kwargs):
        try:
            return self._create_instance(IMCInterface, **kwargs)
        except (ValueError, KeyError):
            raise ValueError("Missing device id and/or interface id")

    def _get_net_asset(self, **kwargs):
        try:
            return self._create_instance(IMCNetAsset, **kwargs)
        except (ValueError, KeyError):
            raise ValueError("Missing network asset")

    def get_resource(self, of_type, **kwargs):
        'creates the various types of iMC resources'
        try:
            if of_type is IMCResourceFactory.TYPE_DEVICE:
                return self._get_device(**kwargs)
            if of_type is IMCResourceFactory.TYPE_VLAN:
                return self._get_vlan(**kwargs)
            if of_type is IMCResourceFactory.TYPE_INTERFACE:
                return self._get_interface(**kwargs)
            if of_type is IMCResourceFactory.TYPE_NETASSET:
                return self._get_net_asset(**kwargs)
            else:
                return None
        except ValueError:
            return None
