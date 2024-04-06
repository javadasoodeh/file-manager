#!/usr/bin/python
# -*- coding: utf-8 -*-
# javadasoodeh73@gmail.com

import json
import logging
from pyramid_storage.exceptions import FileNotAllowed
import uuid
from pyramid.view import view_config
from pyramid.response import Response
from ..classes.mimetypes2ext import MimeTypeToExt
from pyramid_storage import utils
from PIL import Image
from ..models.driver import SysFile


class UploadHandler:
    def __init__(self, request):
        self.request = request
        self.settings = self.request.registry.settings
        self.types = None
        self.extension = None
        self.mimetype = None
        self.d = None
        self.m = None

        # self.logger = logging.getLogger(__name__)
        # self.logger.warning('Inter validation...')

    def validate(self, types):
        self.d = MimeTypeToExt.extension()
        self.m = self.mimetype.lower()
        v = eval(self.settings[types]) and self.m in self.d[types].keys() and self.extension.lower() in self.d[types][
            self.m].split()
        return v

    def file_not_allowed(self, msg="Your File Not Allowed", filename=""):
        response = Response(body=json.dumps({'ERROR': msg, "filename": filename}), status=501)
        return response

    @view_config(route_name='upload', request_method='POST', renderer='json')
    def post(self):
        try:
            # check if the post request has the file part
            if 'upl' not in self.request.POST:
                return self.file_not_allowed()

            # file
            f = self.request.POST.items()

            try:
                for i in f:
                    f = i
                    break
                file_size = len(f[1].value)
            except:
                return self.file_not_allowed()
            # check file size
            if (file_size / 1048576) > int(self.settings['maxuploadsize']):
                response = Response(body=json.dumps({'ERROR': 'Your File Size Not Allowed', "filename": str(f[1].filename)}), status=501)
                return response

            # file name
            file_name_main = f[1].filename
            if '/' in file_name_main or "\\" in file_name_main \
                    or "\"" in file_name_main or "?" in file_name_main or ":" in file_name_main\
                    or "<" in file_name_main or ">" in file_name_main\
                    or "*" in file_name_main or "|" in file_name_main:
                return self.file_not_allowed(msg="Your File Name Is Not True, Please Change Your File Name",
                                             filename=file_name_main)

            # if user does not select file, browser also
            # submit a empty part without filename
            if not file_name_main or '.' not in file_name_main:
                return self.file_not_allowed(filename=file_name_main)

            # content type
            content_type = str(f[1].type)

            # check content_tpe
            if not content_type:
                return self.file_not_allowed(filename=file_name_main)

            f_main = file_name_main.split('.')
            extension_main = f_main[-1]
            file_name_main = "".join(f_main[:-1])
            # check extension
            if not extension_main:
                return self.file_not_allowed(filename=file_name_main)

            self.extension = extension_main
            self.mimetype = content_type

            # access to upload documents or .... and check the Mimetype
            if self.validate('documents'):
                pass
            elif self.validate('archives'):
                pass
            elif self.validate('images'):
                try:
                    Image.open(f[1].file)
                except Exception:
                    # cannot identify image file
                    return self.file_not_allowed(filename=file_name_main)
            elif self.validate('audio'):
                pass
            elif self.validate('video'):
                pass
            else:
                response = Response(body=json.dumps({'ERROR': 'Your File Not Allowed', 'filename': file_name_main}), status=501)
                return response

            try:
                # set id for file name
                f[1].filename = str(uuid.uuid4()) + '.xx'

                # save file
                file_name = self.request.storage.save(f[1], extensions='xx')
                file_name = file_name.split('.')[0]
            except FileNotAllowed:
                return self.file_not_allowed(filename=file_name_main)

            # save details in db
            obj_file = SysFile(fileid=file_name, name_main=file_name_main, content_type=content_type, size=file_size,
                               extension=extension_main)
            inserted = obj_file.insert()
            if not inserted:
                return self.file_not_allowed(filename=file_name_main)

            response = Response(body=json.dumps({'file_id': file_name, 'size': file_size, 'name': file_name}))

            return response
        except Exception as e:
            return self.file_not_allowed()


