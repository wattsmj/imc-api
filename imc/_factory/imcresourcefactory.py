'A module that contains an iMC object resource factory'

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
