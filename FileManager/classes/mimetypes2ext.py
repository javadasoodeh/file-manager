"""
    Title : convert ContentType to Extension
    Author : Javad Asoodeh
    Date : 9-20-2016
"""

# inspired by https://codex.wordpress.org/Function_Reference/get_allowed_mime_types

"""
array(
	// Image formats
	'jpg|jpeg|jpe'                 => 'image/jpeg',
	'gif'                          => 'image/gif',
	'png'                          => 'image/png',
	'bmp'                          => 'image/bmp',
	'tif|tiff'                     => 'image/tiff',
	'ico'                          => 'image/x-icon',

	// Video formats
	'asf|asx'                      => 'video/x-ms-asf',
	'wmv'                          => 'video/x-ms-wmv',
	'wmx'                          => 'video/x-ms-wmx',
	'wm'                           => 'video/x-ms-wm',
	'avi'                          => 'video/avi',
	'divx'                         => 'video/divx',
	'flv'                          => 'video/x-flv',
	'mov|qt'                       => 'video/quicktime',
	'mpeg|mpg|mpe'                 => 'video/mpeg',
	'mp4|m4v'                      => 'video/mp4',
	'ogv'                          => 'video/ogg',
	'webm'                         => 'video/webm',
	'mkv'                          => 'video/x-matroska',
	
	// Text formats
	'txt|asc|c|cc|h'               => 'text/plain',
	'csv'                          => 'text/csv',
	'tsv'                          => 'text/tab-separated-values',
	'ics'                          => 'text/calendar',
	'rtx'                          => 'text/richtext',
	'css'                          => 'text/css',
	'htm|html'                     => 'text/html',
	
	// Audio formats
	'mp3|m4a|m4b'                  => 'audio/mpeg',
	'ra|ram'                       => 'audio/x-realaudio',
	'wav'                          => 'audio/wav',
	'ogg|oga'                      => 'audio/ogg',
	'mid|midi'                     => 'audio/midi',
	'wma'                          => 'audio/x-ms-wma',
	'wax'                          => 'audio/x-ms-wax',
	'mka'                          => 'audio/x-matroska',
	
	// Misc application formats
	'rtf'                          => 'application/rtf',
	'js'                           => 'application/javascript',
	'pdf'                          => 'application/pdf',
	'swf'                          => 'application/x-shockwave-flash',
	'class'                        => 'application/java',
	'tar'                          => 'application/x-tar',
	'zip'                          => 'application/zip',
	'gz|gzip'                      => 'application/x-gzip',
	'rar'                          => 'application/rar',
	'7z'                           => 'application/x-7z-compressed',
	'exe'                          => 'application/x-msdownload',
	
	// MS Office formats
	'doc'                          => 'application/msword',
	'pot|pps|ppt'                  => 'application/vnd.ms-powerpoint',
	'wri'                          => 'application/vnd.ms-write',
	'xla|xls|xlt|xlw'              => 'application/vnd.ms-excel',
	'mdb'                          => 'application/vnd.ms-access',
	'mpp'                          => 'application/vnd.ms-project',
	'docx'                         => 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	'docm'                         => 'application/vnd.ms-word.document.macroEnabled.12',
	'dotx'                         => 'application/vnd.openxmlformats-officedocument.wordprocessingml.template',
	'dotm'                         => 'application/vnd.ms-word.template.macroEnabled.12',
	'xlsx'                         => 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
	'xlsm'                         => 'application/vnd.ms-excel.sheet.macroEnabled.12',
	'xlsb'                         => 'application/vnd.ms-excel.sheet.binary.macroEnabled.12',
	'xltx'                         => 'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
	'xltm'                         => 'application/vnd.ms-excel.template.macroEnabled.12',
	'xlam'                         => 'application/vnd.ms-excel.addin.macroEnabled.12',
	'pptx'                         => 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
	'pptm'                         => 'application/vnd.ms-powerpoint.presentation.macroEnabled.12',
	'ppsx'                         => 'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
	'ppsm'                         => 'application/vnd.ms-powerpoint.slideshow.macroEnabled.12',
	'potx'                         => 'application/vnd.openxmlformats-officedocument.presentationml.template',
	'potm'                         => 'application/vnd.ms-powerpoint.template.macroEnabled.12',
	'ppam'                         => 'application/vnd.ms-powerpoint.addin.macroEnabled.12',
	'sldx'                         => 'application/vnd.openxmlformats-officedocument.presentationml.slide',
	'sldm'                         => 'application/vnd.ms-powerpoint.slide.macroEnabled.12',
	'onetoc|onetoc2|onetmp|onepkg' => 'application/onenote',
	
	// OpenOffice formats
	'odt'                          => 'application/vnd.oasis.opendocument.text',
	'odp'                          => 'application/vnd.oasis.opendocument.presentation',
	'ods'                          => 'application/vnd.oasis.opendocument.spreadsheet',
	'odg'                          => 'application/vnd.oasis.opendocument.graphics',
	'odc'                          => 'application/vnd.oasis.opendocument.chart',
	'odb'                          => 'application/vnd.oasis.opendocument.database',
	'odf'                          => 'application/vnd.oasis.opendocument.formula',
	
	// WordPerfect formats
	'wp|wpd'                       => 'application/wordperfect',
	
	// iWork formats
	'key'                          => 'application/vnd.apple.keynote',
	'numbers'                      => 'application/vnd.apple.numbers',
	'pages'                        => 'application/vnd.apple.pages',
)

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
        cls.extensions['documents']['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'] = 'xlsx'

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
