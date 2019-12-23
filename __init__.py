#!/usr/bin/python
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop

from pyramid.config import Configurator  # boot
from FileManager.classes.config import Config
import configparser
from FileManager.models.meta import MyRequest

settings = configparser.ConfigParser()
settings.read("D:/projects/settings/config/FileManager.ini")
main_settings = dict(settings.items('app:main'))
server = dict(settings.items('server:main'))


def main(**settings):
    # create object of configurator
    with Configurator(settings=settings) as config:
        # close db connection after every request
        config.set_request_factory(MyRequest)

        # settings
        settings = config.registry.settings

        # urls
        url_location = settings['setting_folder'] + '/to_srv_urls/FileManager.properties'

        # add subscribers
        config.add_subscriber('FileManager.subscribers.my_custom_subscriber', 'pyramid.events.NewRequest')

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
    container = tornado.wsgi.WSGIContainer(main(**main_settings))
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(int(server['port']))
    tornado.ioloop.IOLoop.instance().start()
