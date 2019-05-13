'''
A module that contains the abstract base class to access the iMC API
'''

from abc import ABCMeta, abstractmethod
from . import IMCRequest

class IMCResource(IMCRequest):
    '''
    Provides a high level abstraction of
    query tasks to retrieve an individual resource from iMC
    '''
    __metaclass__ = ABCMeta

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super(IMCResource, self).__init__(baseurl, username, password, **kwargs)
        self._data = None

    def _get_data(self, item):
        'Returns values from the iMC API response as instance attributes'
        if self._data is not None:
            if self._data.get(item, False):
                return self._data.get(item)

    def __getattr__(self, item):
        'Returns self._get_data() via native attribute'
        return self._get_data(item)

    @abstractmethod
    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'
        pass

    def get_resource(self, **kwargs):
        'Executes the API call to iMC and saves the results in self._data'
        try:
            self._get_resource(**kwargs)
        except KeyError:
            raise ValueError('Missing required identifier')
        self._data = self._callapi()
