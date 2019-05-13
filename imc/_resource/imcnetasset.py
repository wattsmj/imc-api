'''
A module that contains the base class to access the iMC API
'''

from imc._abc import IMCResource


class IMCNetAsset(IMCResource):
    'Returns the details of a netasset in iMC filtered by advanced query'

    def __init__(self, baseurl, username, password):
        'Initialise the object'

        super(IMCNetAsset, self).__init__(baseurl, username, password)
        self._api = '/imcrs/netasset/asset'
        self._content = IMCResource._CONTENT_JSON
        self._serial = None

    @property
    def serial(self):
        'Getter for serial'
        return self._serial

    @serial.setter
    def serial(self, value):
        'Setter for serial'
        if type(value) is str:
            self._serial = value
        else:
            raise ValueError("Serials must be a string")

    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'

        if self._serial is not None:
            self._options = {'assetSerialNum': self._serial}

    def _get_data(self, item):
        'Returns values from the iMC API response as instance attributes'

        if 'netAsset' not in self._data:
            raise AttributeError(f'No data')

        netasset = self._data['netAsset']

        if type(netasset) is list:
            for chassis in netasset:
                if item in chassis:
                    return chassis[item]

        if type(netasset) is dict:
            if item not in netasset:
                raise AttributeError(f'No attribute {item}')
            return netasset[item]
