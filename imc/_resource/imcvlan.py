'''
A module that contains the base class to access the iMC API
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
