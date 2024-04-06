from peewee import *
from pyramid.request import Request
import configparser

# read ini file
settings = configparser.ConfigParser()
settings.read("D:\\projects\\file-manager\\configs\\config\\FileManager.ini")
db = dict(settings.items('database'))

# database
database = MySQLDatabase(
    str(db['database']), host=str(db['host']), port=int(db['port']), user=str(db['user']), passwd=str(db['password']))


class MyModel(Model):
    class Meta:
        database = database


class MyRequest(Request):
    def __init__(self, environ, *args, **kwargs):
        super(MyRequest, self).__init__(environ, **kwargs)
        try:
            if database.is_closed():
                database.connect()
                # print 'open connection DB'
        except Exception as e:
            print("DBCanNotConnectERROR !!! FileManager.models.meta : ", e)

        self.add_finished_callback(self.finish)

    def finish(self, request):
        if not database.is_closed():
            database.close()
            # print "close connection DB"

