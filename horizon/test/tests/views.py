# Copyright 2015 Cisco Systems, Inc.
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

from horizon.test import helpers as test
from horizon import views

FAKENAME = "FakeName"


class FakeTemplate(object):

    def get_context_data(self):
        return {}


class NamedObject(object):
    name = FAKENAME


class PageWithNoTitle(views.PageTitleMixin, FakeTemplate):
    pass


class PageWithGetData(views.PageTitleMixin, FakeTemplate):
    page_title = "A Title"

    def get_data(self):
        return NamedObject()


class PageTitleTests(test.TestCase):

    def test_no_title_set(self):
        page = PageWithNoTitle()
        data = page.get_context_data()
        self.assertEqual("", data['page_title'])

    def test_data_source(self):
        page = PageWithGetData()
        data = page.get_context_data()
        self.assertEqual(page.page_title, data['page_title'])
