#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
# from weasyprint import HTML, CSS
# from weasyprint.fonts import FontConfiguration
#

class PDF:
    def __init__(self, path='../files/', filename=None, html=None, stylesheets=None, string=False):
        self.filename = filename
        self.html = html
        self.stylesheets = stylesheets
        self.path = path
        self.string = string

    def html_to_pdf(self):
        try:
            # font_config = FontConfiguration()
            # html = HTML(self.html) if not self.string else HTML(string=self.html)
            # html.write_pdf(self.path + self.filename, stylesheets=[CSS(self.stylesheets)] if self.stylesheets else None, font_config=font_config)
            size = os.path.getsize( self.path + self.filename)
        except Exception as e:
            logging.getLogger('root').warning(str(e))
            return False
        return size

