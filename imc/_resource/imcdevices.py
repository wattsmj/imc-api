'''
A module that contains the base class to access the iMC API
'''

from imc._abc import IMCResource

class IMCDevices(IMCResource):
    'Returns the details of a device in iMC by device ID'

    def __init__(self, baseurl, username, password):
        'Initialise the object'
        super(IMCResource, self).__init__(baseurl, username, password)
        self._api = '/imcrs/plat/res/device'
        self._content = IMCResource._CONTENT_JSON

    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'
        if kwargs.get('label'):
            self._options = {'label': kwargs['label']}

    def _get_data(self, item):
        'Returns values from the iMC API response as instance attributes'

        if self._data is type(list):
            return None
        
        if self._data is not None:
            data = self._data['device']
            if data.get(item, False):
                return data.get(item)