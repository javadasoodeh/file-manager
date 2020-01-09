#!/usr/bin/python
# -*- coding: utf-8 -*-
# javadasoodeh73@gmail.com

import json
import os

from pyramid.view import view_config
from pyramid.response import FileResponse, Response
from pyramid.httpexceptions import HTTPNotFound
from ..models.driver import SysFile
import pdfkit
import uuid


class DownloadHandler:
    def __init__(self, request):
        self.request = request
        self.settings = self.request.registry.settings

    def generate_pdf(self, html, name, opt=None):
        if opt is None:
            opt = {}
        config = pdfkit.configuration(wkhtmltopdf=self.settings['wkhtmltopdf_path'])
        options = {
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-left': '0',
            'margin-bottom': '0',
            'zoom': '1.2',
            'encoding': "UTF-8",
            'footer-right': '[page]',
            'cookie': list(self.request.cookies._cache.items())

        }

        options.update(opt)
        _path = os.path.join(self.settings['storage.base_path'], name)
        _status = pdfkit.from_string(html, _path, configuration=config, options=options)

        return _path if _status else ''

    @view_config(route_name='download', request_method='GET')
    def get(self):
        file_id = self.request.matchdict['fileid']
        obj_file = SysFile(fileid=file_id)
        f = obj_file.get_one()
        if not f:
            raise HTTPNotFound
        r = FileResponse(self.request.storage.path(file_id + '.xx'))
        r.content_disposition = 'attachment; filename="{f}.{e}"'.format(f=f['name_main'], e=f['extension'])
        r.content_type = '{c}'.format(c=f['content_type'])
        r.content_length = int(f['size'])
        # internet Explorer
        r.cache_control = 'public'
        return r

    @view_config(route_name='URLToPDF', request_method='POST')
    def url_to_pdf(self):
        html = self.request.params.get('html', None)
        file_name_main = 'asdf'
        opt = json.loads(self.request.params.get('opt', '{}'))
        # create a file name by uuid
        file_id = str(uuid.uuid4())
        file_name = file_id + '.xx'
        # generate a pdf file from url
        path = self.generate_pdf(html, file_name, opt)
        # get file size
        file_size = os.path.getsize(path)
        # pdf content type
        content_type = 'application/pdf'

        # save details in db
        obj_file = SysFile(fileid=file_id, name_main=file_name_main, content_type=content_type, size=file_size,
                           extension='pdf')
        inserted = obj_file.insert()
        if not inserted:
            return Response(body='Please Contact to your administrator', status=500)

        response = Response(body=json.dumps({'file_id': file_id, 'size': file_size, 'name': file_name_main}))

        return response

    @view_config(route_name='URLToPDF', request_method='OPTIONS')
    def options(self):
        response = Response()
        return response

        # return file
        # r = FileResponse(path)
        # r.content_disposition = 'attachment; filename="{f}.pdf"'.format(f=file_name_main)
        # r.content_type = '{c}'.format(c=content_type)
        # r.content_length = int(file_size)
        # # internet Explorer
        # r.cache_control = 'public'

        # remove file
        # if os.path.exists(path):
        #     os.remove(path)

        # return r
