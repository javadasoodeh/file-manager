#!/usr/bin/python
from pyramid.config import Configurator  # boot
from FileManager.classes.config import Config
from FileManager.models.meta import MyRequest
import configparser
import tornado.ioloop
import tornado.wsgi
from tornado.httpserver import HTTPServer
from pyramid.paster import setup_logging
import logging


__author__ = 'javadasoodeh73@gmail.com'

# read ini file
settings = configparser.ConfigParser()
settings.read("C:\\Users\\asoodeh.j\\Desktop\\python-projects\\file-manager\\configs\\config\\FileManager.ini")
main_settings = dict(settings.items('app:main'))
server_settings = dict(settings.items('server:main'))


def main(**settings):
    # create object of configurator
    with Configurator(settings=settings) as config:
        # create object of configurator

        config.set_request_factory(MyRequest)

        # logging
        # setup_logging('D:\\projects\\file-manager\\configs\\config\\FileManager.ini')
        logging.basicConfig(level=logging.DEBUG)

        # cors
        config.include('FileManager.classes.cors')

        # make sure to add this before other routes to intercept OPTIONS
        config.add_cors_preflight_handler()



        # config.add_subscriber(my_custom_subscriber, 'pyramid.events.NewResponse')

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



if __name__ == '__main__':
    c = tornado.wsgi.WSGIContainer(main(**main_settings))
    http_server = HTTPServer(c)
    http_server.listen(int(server_settings.get('port')))
    tornado.ioloop.IOLoop.instance().start()
    # server = make_server(server_settings['host'], int(server_settings['port']), main(**main_settings))
    # server.serve_forever()

