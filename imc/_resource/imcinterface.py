'''
A convience-style partial front-end to the iMC REST API (IMCRS) written in Python 3.
Copyright (C) 2019  Matthew Watts

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Author: wattsmj
Contact: Please raise an issue on www.github.com/wattsmj/imc-api
Description: A module that contains the base class to access the iMC API
'''

from imc._abc import IMCResource


class IMCInterface(IMCResource):
    'Returns the details of a vlan in iMC by device ID'

    def __init__(self, baseurl, username, password, **kwargs):
        'Initialise the object'
        super().__init__(baseurl, username, password)
        self._api = '/imcrs/plat/res/device/{device_id}/interface/{interface_id}'
        self._content = IMCResource._CONTENT_JSON

    def _get_data(self, item):
        'Returns values from the iMC API response as instance attributes'
        try:
            if 'ipHash' in self._data:
                # Special computed values because the JSON is convoluted
                if item == 'ip_address':
                    index = 0
                elif item == 'netmask':
                    index = 1
                else:
                    # Return a direct value that was part of the JSON reply
                    return self._data[item]
                return self._data['ipHash']['item'][index]
        except TypeError:
            # Secondary IP on the interface
            if item == 'ip_address':
                index = 0
            elif item == 'netmask':
                index = 1
            else:
                raise AttributeError(f'No attribute {item}')
            return [iphash['item'][index] for iphash in self._data['ipHash']]
        except (AttributeError, KeyError, IndexError):
            raise AttributeError(f'No attribute {item}')

    def _get_resource(self, **kwargs):
        'Private method that prepares the instance for the api call'
        self._api = self._api.format(
            device_id=kwargs['device_id'],
            interface_id=kwargs['interface_id']
        )
        self._options.update({'size': 1000})
