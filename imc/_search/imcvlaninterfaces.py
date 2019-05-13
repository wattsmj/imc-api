'''
A module that contains the IMCSubnets class to access the iMC API device Ids
'''

# Collections
from collections import namedtuple

# Netaddr imports
from netaddr import IPNetwork
from netaddr.core import AddrFormatError

# Dependant IMC imports
from imc._abc import IMCIterable
from . import IMCDeviceIDs


class IMCVlanInterfaces(IMCIterable):
    'Get method returns all the iMC subnets'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super(IMCVlanInterfaces, self).__init__(baseurl, username, password, **kwargs)
        self._api = '/imcrs/vlan/vlanif'
        self._content = IMCIterable._CONTENT_JSON
        self._imcdevices = None

    def _convert_imcdict_to_cidr(self, vlanif):
        'Adapter for returned iMC REST dict into a CIDR'
        try:
            ip_address = vlanif['ipAddress']
            mask = vlanif['ipMask']
            return str(IPNetwork(ip_address + '/' + mask).cidr)
        except (TypeError, KeyError, AddrFormatError) as ex:
            raise ex

    def get_resource(self):
        '''
        Uses callapi to retrieve the list of devices
        then pulls out IDs and stores them
        '''
        if self._data is None:
            self._data = []
            # Make sure we can call the devices iterator
            if self._imcdevices is None:
                self._imcdevices = IMCDeviceIDs(
                    baseurl=self._baseurl,
                    username=self._username,
                    password=self._password,
                    **self._options
                )
            # Process each device ID and retrieve the subnets that belong to that device
            for device_id in self._imcdevices:
                # Call iMC with the current device ID and get a list of it's vlan interfaces
                self._options.update({'devId': str(device_id)})
                resp = self._callapi()
                # Extract IP Subnet from the iMC reponse and store it in self._data
                # as a namedtuple
                try:
                    subnet = namedtuple('subnet', 'device_id, cidr')
                    subnet.device_id = device_id
                    for vlanif in resp['vlanIf']:
                        try:
                            subnet.cidr = self._convert_imcdict_to_cidr(vlanif)
                            self._data.append(subnet)
                        except (TypeError, KeyError):
                            # Only a single record returned.
                            # We'll have a list of the keys in that dict,
                            # so go back, get the dict itself and convert it and break the loop
                            vlanif = resp['vlanIf']
                            subnet.cidr = self._convert_imcdict_to_cidr(vlanif)
                            self._data.append(subnet)
                            break
                        except AddrFormatError:
                            ip_address = vlanif['ipAddress']
                            mask = vlanif['ipMask']
                            subnet.cidr = f'{ip_address}/{mask}'
                            self._data.append(subnet)
                            continue
                    # Remove the residual option from self._options
                    self._options.pop('devId', None)
                except KeyError:
                    # Blank response, no vlan interfaces match the device
                    continue
