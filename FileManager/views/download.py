#!/usr/bin/python
# -*- coding: utf-8 -*-
# javadasoodeh73@gmail.com
import json
import os

from pyramid.view import view_config
from pyramid.response import FileResponse, Response
from pyramid.httpexceptions import HTTPNotFound
from ..models.driver import SysFile


class DownloadHandler:
    def __init__(self, request):
        self.request = request
        self.settings = self.request.registry.settings

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
