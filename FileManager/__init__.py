#!/usr/bin/python
from pyramid.config import Configurator  # boot
from FileManager.classes.config import Config
from FileManager.models.meta import MyRequest
import configparser
import tornado.ioloop
import tornado.wsgi
from tornado.httpserver import HTTPServer

__author__ = 'javadasoodeh73@gmail.com'

# read ini file
settings = configparser.ConfigParser()
settings.read("C:\\workflow-sys\\file-manager\\configs\\config\\FileManager.ini")
main_settings = dict(settings.items('app:main'))
server_settings = dict(settings.items('server:main'))




def main(**settings):
    # create object of configurator
    with Configurator(settings=settings) as config:
        # create object of configurator

        config.set_request_factory(MyRequest)

        # settings
        settings = config.registry.settings

        # urls
        url_location = settings['setting_folder'] + '/to_srv_urls/FileManager.properties'

        get_urls = Config(properties_file_path=url_location)
        urls = get_urls.urls_()

        for route in urls:
            config.add_route(route, urls[route])

        # scanning views
        config.scan('FileManager.views')

        """ create a web server / host name && port && ... """
        app = config.make_wsgi_app()
        application = app
        return application



from tornado.autoreload import add_reload_hook, start

if __name__ == '__main__':
    c = tornado.wsgi.WSGIContainer(main(**main_settings))
    http_server = HTTPServer(c)
    http_server.listen(int(server_settings.get('port')))
    start()

    tornado.ioloop.IOLoop.instance().start()
    # server = make_server(server_settings['host'], int(server_settings['port']), main(**main_settings))
    # server.serve_forever()

