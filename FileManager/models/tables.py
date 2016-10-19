from .meta import *


class File(MyModel):
    fileid = CharField(primary_key=True)
    name_main = CharField()
    content_type = CharField()
    size = IntegerField()
    extension = CharField()
