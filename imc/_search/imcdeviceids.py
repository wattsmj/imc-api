'''
A module that contains the IMCdeviceIDs class to access the iMC API device Ids
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
