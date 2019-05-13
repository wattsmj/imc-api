'''
A module that contains the base class to access the iMC API
'''

from imc._abc import IMCResource

class IMCDevice(IMCResource):
    'Returns the details of a device in iMC by device ID'

    def __init__(self, baseurl, username, password):
        'Initialise the object'
        super(IMCDevice, self).__init__(baseurl, username, password)
        self._api = '/imcrs/plat/res/device/{id}'
        self._content = IMCResource._CONTENT_JSON

    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'
        self._api = self._api.format(id=kwargs['device_id'])
