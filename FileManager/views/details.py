#!/usr/bin/python
# -*- coding: utf-8 -*-
# javadasoodeh73@gmail.com
import json

from pyramid.view import view_config
from pyramid.response import Response
from ..models.driver import SysFile


class DetailsHandler:
    def __init__(self, request):
        self.request = request
        self.settings = self.request.registry.settings

    @view_config(route_name='details', request_method='POST', renderer='json')
    def post(self):
        files = json.loads(self.request.body)['files']
        obj_system_file = SysFile(files=files)
        ret = obj_system_file.get_particular_files()
        if ret is False:
            return Response(status=500)
        return Response(body=json.dumps(ret))
