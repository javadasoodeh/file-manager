from peewee import *
from pyramid.request import Request
import configparser

# read ini file
settings = configparser.ConfigParser()
settings.read("/var/website/WebIFace/WebIFace/quesionBank/config/FileManager.ini")
db = dict(settings.items('database'))

# database
database = MySQLDatabase(
    str(db['database']), host=str(db['host']), port=int(db['port']), user=str(db['user']), passwd=str(db['password']))


class MyRequest(Request):
    def __init__(self, environ, *args, **kwargs):
        super(MyRequest, self).__init__(environ, **kwargs)
        try:
            database.connect()
            # print 'open connection DB'
        except Exception, e:
            print("DBCanNotConnectERROR !!! file-manger.models.meta : ", e)

        self.add_finished_callback(self.finish)

    def finish(self, request):
        if not database.is_closed():
            database.close()
            # print "close connection DB"


class MyModel(Model):
    class Meta:
        database = database
