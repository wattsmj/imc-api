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
Description: A module that contains an iMC object factory for Iterable instances
'''

from imc._search import (
    IMCDeviceIDs,
    IMCVlanInterfaces,
    IMCDevicesWithVLAN,
    IMCInterfaces
)


class IMCIterableFactory(object):
    '''
    A factory class that returns IMC objects that 
    select the records of a selected type from iMC
    '''

    TYPE_ALLDEVICEID = 'device_ids'
    TYPE_ALLVLANINTERFACES = 'vlaninterfaces'
    TYPE_DEVICESWITHVLAN = 'devices_with_vlan'
    TYPE_INTERFACESBYDEVICE = 'interfaces_by_device'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise instance variables'
        self._baseurl = baseurl
        self._username = username
        self._password = password
        self._options = kwargs

    def _create_instance(self, class_type, deferred_query):
        '''
        Creates an Iterable instance of the given class type
        runs the query if required and returns it
        '''
        # Create an instance of the type
        instance = class_type(
            baseurl=self._baseurl,
            username=self._username,
            password=self._password,
            **self._options
        )
        # Do an eager query if requested
        if deferred_query is False:
            instance.get_resource()
        # Return the instance
        return instance

    def get_subnets(self, of_type, deferred_query=True):
        '''
        Works out the type of object that returns subnets to create, then
        initialises and returns it
        '''
        if of_type is self.TYPE_ALLVLANINTERFACES:
            class_type = IMCVlanInterfaces
        else:
            return None
        return self._create_instance(class_type, deferred_query)

    def get_device_ids(self, of_type, deferred_query=True):
        '''
        Works out the type of object that returns device IDs to create, then
        initialises and returns it
        '''
        # Select the type supported by this factory
        if of_type is self.TYPE_ALLDEVICEID:
            class_type = IMCDeviceIDs
        elif of_type is self.TYPE_DEVICESWITHVLAN:
            class_type = IMCDevicesWithVLAN
        else:
            return None
        return self._create_instance(class_type, deferred_query)

    def get_interface_ids(self, of_type, deferred_query=True):
        '''
        Works out the type of object that returns interface IDs to create, then
        initialises and returns it
        '''
        # Select the type supported by this factory
        if of_type is self.TYPE_INTERFACESBYDEVICE:
            class_type = IMCInterfaces
        else:
            return None
        return self._create_instance(class_type, deferred_query)       