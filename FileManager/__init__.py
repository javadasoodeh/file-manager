#!/usr/bin/python
from pyramid.config import Configurator  # boot
from classes.config import Config


def main(global_config, **settings):
    # create object of configurator
    config = Configurator(settings=settings)

    # settings
    settings = config.registry.settings

    # urls
    url_location = settings['setting_folder'] + '\\to_srv_urls\\FileManager.properties'

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
