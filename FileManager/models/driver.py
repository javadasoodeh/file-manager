#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FileManager.models.tables import File

__author__ = 'j4v4d'


class SysFile:
    def __init__(self, fileid=None, name_main=None, content_type=None, size=None, extension=None, files=None):
        if not files:
            files = []
        self.files = files
        self.fileid = fileid
        self.name_main = name_main
        self.content_type = content_type
        self.size = size
        self.extension = extension

    def insert(self):
        try:
            File.insert(
                fileid=self.fileid,
                name_main=self.name_main,
                content_type=self.content_type,
                size=self.size,
                extension=self.extension
            ).execute()
            return True
        except:
            return False

    def get_all(self):
        try:
            x = File.select()
            ls = []
            for i in x:
                ls.append(
                    dict(
                        fileid=i.fileid,
                        name_main=i.name_main,
                        content_type=i.content_type,
                        size=i.size,
                        extension=i.extension
                    )
                )
            return ls
        except Exception, e:
            print(e)
            return []

    def get_one(self):
        try:
            i = File.get(File.fileid == self.fileid)
            return dict(
                fileid=i.fileid,
                name_main=i.name_main,
                content_type=i.content_type,
                size=i.size,
                extension=i.extension
            )
        except Exception, e:
            return dict()

    def get_particular_files(self):

        try:
            selected = File.select().where(File.fileid << self.files)
            return [dict(
                fileid=i.fileid,
                name_main=i.name_main,
                content_type=i.content_type,
                size=i.size,
                extension=i.extension
            )for i in selected]
        except Exception, e:
            return False

    def delete(self):
        try:
            x = File.delete().where(File.fileid == self.fileid).execute()
            return True
        except Exception, e:
            return False
