'''
A module that contains the abstract base class to access the iMC API
'''

from abc import ABCMeta
import requests
from requests.auth import HTTPDigestAuth


class IMCRequest(object):
    'Provides a high level abstraction of query tasks to perform against iMC'
    __metaclass__ = ABCMeta

    _CONTENT_JSON = 'json'
    _CONTENT_XML = 'xml'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        self._baseurl = baseurl
        self._username = username
        self._password = password
        self._options = kwargs
        self._api = None
        self._content = None

    def _callapi(self):
        'Takes an api url and queries iMC and returns the results'

        # Create the options string
        optionsurl = '?' + '&'.join(
            ['='.join([key, str(value)]) for key, value in self._options.items()]
        )

        # Submit the request to iMC
        result = requests.get(
            self._baseurl + self._api + optionsurl,
            auth=HTTPDigestAuth(self._username, self._password),
            headers={'Accept': 'application/' + self._content}
        )

        # Return
        if result.status_code == 200:
            if self._content == IMCRequest._CONTENT_JSON:
                return result.json()
            elif self._content == IMCRequest._CONTENT_XML:
                return result.text
        else:
            return []
