# Copyright 2014 Cisco Systems, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import json


class JSONCookieEntry(dict):
    def __init__(self, request, entry, response=None):
        self.request = request
        self.response = response
        self.entry = entry
        try:
            data = json.loads(self.request.COOKIES.get(entry, ""))
        except (TypeError, ValueError):
            data = {}
        super(JSONCookieEntry, self).__init__(data)

    def __setitem__(self, name, item):
        if self.response:
            super(JSONCookieEntry, self).__setitem__(name, item)
            self.response.set_cookie(self.entry, json.dumps(self))
        else:
            raise TypeError('Without a response object this entry is readonly')
