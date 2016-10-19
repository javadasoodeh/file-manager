"""
    Title : convert ContentType to Extension
    Author : Javad Asoodeh
    Date : 9-20-2016
"""


class MimeTypeToExt:
    def __init__(self):
        pass

    @classmethod
    def extension(cls):
        cls.extensions = {'text': {}, 'documents': {}, 'images': {}, 'audio': {}, 'video': {}, 'data': {},
                          'scripts': {}, 'archives': {}, 'executables': {}}

        cls.extensions['documents']['application/pdf'] = 'pdf'
        cls.extensions['documents']['application/rtf'] = 'rtf'
        cls.extensions['documents']['application/vnd.oasis.opendocument.formula'] = 'odf'
        cls.extensions['documents']['application/vnd.oasis.opendocument.spreadsheet'] = 'ods'
        cls.extensions['documents']['application/x-gnumeric'] = 'gnumeric'
        cls.extensions['documents']['application/x-abiword'] = 'abw'
        cls.extensions['documents']['application/msword'] = 'doc'
        cls.extensions['documents']['application/vnd.openxmlformats-officedocument.wordprocessingml.document'] = 'docx'
        cls.extensions['documents']['application/vnd.ms-excel'] = 'xls'

        cls.extensions['images']['image/jpeg'] = 'jpg jfif jfif-tbnl jpe jpeg'
        cls.extensions['images']['image/png'] = 'png x-png'
        cls.extensions['images']['image/gif'] = 'gif'
        cls.extensions['images']['image/svg+xml'] = 'svg'
        cls.extensions['images']['image/bmp'] = 'bmp bm'
        cls.extensions['images']['image/tiff'] = 'tiff tif'

        cls.extensions['audio']['audio/x-wav'] = 'wav'
        cls.extensions['audio']['audio/mpeg'] = 'mp3'
        cls.extensions['audio']['audio/x-aac'] = 'aac'
        cls.extensions['audio']['audio/ogg'] = 'ogg oga'
        cls.extensions['audio']['audio/flac'] = 'flac'

        cls.extensions['video']['video/mpeg'] = 'mpeg'
        cls.extensions['video']['video/3gpp'] = '3gp'
        cls.extensions['video']['video/x-msvideo'] = 'avi'
        cls.extensions['video']['video/divx'] = 'divx'
        cls.extensions['video']['video/x-flv'] = 'flv'
        cls.extensions['video']['video/mp4'] = 'mp4'
        cls.extensions['video']['video/x-ms-wmv'] = 'wmv'

        cls.extensions['archives']['application/x-gzip'] = 'gz'
        cls.extensions['archives']['application/x-bzip2'] = 'bz2'
        cls.extensions['archives']['application/x-compressed'] = 'zip'
        cls.extensions['archives']['application/x-zip-compressed'] = 'zip'
        cls.extensions['archives']['application/zip'] = 'zip'
        cls.extensions['archives']['multipart/x-zip'] = 'zip'
        cls.extensions['archives']['application/x-tar'] = 'tar'
        cls.extensions['archives']['application/gnutar'] = 'tgz'

        return cls.extensions
