#!/usr/bin/python
# -*- coding: utf-8 -*-
# javadasoodeh73@gmail.com

import json
import uuid
from pyramid.view import view_config
from pyramid.response import Response
from ..classes.pdf_production import PDF

from ..models.driver import SysFile


class HTMLToPDFHandler:
    def __init__(self, request):
        self.request = request
        self.settings = self.request.registry.settings

    @view_config(route_name='html_to_pdf', request_method='POST', renderer='json')
    def post(self):
        filename_main = self.request.params.get('filename_main', None)
        html = self.request.params.get('html', None)
        stylesheets = self.request.params.get('stylesheets', None)
        string = json.loads(self.request.params.get('string', ''))

        if not filename_main or not html or string not in [True, False]:
            return Response(status=500)

        # create a unique file name
        filename_id = str(uuid.uuid4()) + '.xx'

        # convert html to pdf file
        pdf_size = PDF(path=self.settings['storage.base_path'], filename=filename_id, html=html,
                       stylesheets=stylesheets, string=string).html_to_pdf()
        if not pdf_size:
            return Response(status=500)

        # save details in db
        obj_file = SysFile(fileid=filename_id, name_main=filename_main, content_type='application/pdf', size=pdf_size,
                           extension='pdf')
        inserted = obj_file.insert()
        if not inserted:
            return Response(status=500)

        message = {'filename_id': filename_id}
        response = Response(body=json.dumps(message), status=200)
        return response
