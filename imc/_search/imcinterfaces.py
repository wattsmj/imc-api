'''
A module that contains the IMCInterfaces class to access the iMC API device Ids
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
