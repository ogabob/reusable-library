#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from pages import Page, Page2
from library import input

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p2 = Page2()
        info = input()
        info.__make = self.request.GET['make']
        info.model = self.request.GET['model']
        info.year = self.request.GET['year']
        info.body_style = self.request.GET['bds']
        info.vin = self.request.GET['vin']
        info.miles = self.request.GET['miles']


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
