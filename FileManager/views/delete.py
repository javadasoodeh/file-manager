#!/usr/bin/python
# -*- coding: utf-8 -*-
# javadasoodeh73@gmail.com
import json
import os
from pyramid.view import view_config
from pyramid.response import Response
from ..models.driver import SysFile


class DeleteHandler:
    def __init__(self, request):
        self.request = request
        self.settings = self.request.registry.settings

    @view_config(route_name='delete', request_method='POST')
    def delete(self):
        data = json.loads(self.request.body.decode())
        file_id = str(data['file_id']).strip()
        obj_file = SysFile(fileid=file_id)
        f = obj_file.delete()
        if not f:
            return Response(body=json.dumps({'ERROR': 'Not Found'}))
        path = self.request.storage.path(file_id + '.xx')
        if os.path.exists(path):
            os.remove(path)
        return Response(body=json.dumps({'data': 'deleted success'}))
