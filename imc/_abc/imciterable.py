'''
A module that contains the base iterable class to access the iMC API
'''

from abc import ABCMeta, abstractmethod
from collections import Iterable
from . import IMCRequest


class IMCIterable(IMCRequest, Iterable):
    '''
    Provides a high level abstraction of query tasks
    to perform against iMC presented as an Iterable instance
    '''
    __metaclass__ = ABCMeta

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super(IMCIterable, self).__init__(baseurl, username, password, **kwargs)
        self._data = None

    def __iter__(self):
        # Check for data and load if there is none
        if self._data is None:
            self.get_resource()
        # Use yield to provide an iterator over _data
        for item in self._data:
            yield item

    @abstractmethod
    def get_resource(self):
        'Makes the call to iMC and stores the response in self._data'
        pass
