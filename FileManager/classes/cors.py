from pyramid.security import NO_PERMISSION_REQUIRED


def includeme(config):
    config.add_directive(
        'add_cors_preflight_handler', add_cors_preflight_handler)
    config.add_route_predicate('cors_preflight', CorsPreflightPredicate)

    config.add_subscriber(add_cors_to_response, 'pyramid.events.NewResponse')


class CorsPreflightPredicate(object):
    def __init__(self, val, config):
        self.val = val

    def text(self):
        return 'cors_preflight = %s' % bool(self.val)

    phash = text

    def __call__(self, context, request):
        if not self.val:
            return False
        return (
                request.method == 'OPTIONS' and
                'HTTP_ORIGIN' in request.headers.environ and
                'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.headers.environ
        )


def add_cors_preflight_handler(config):
    config.add_route(
        'cors-options-preflight', '/{catch_all:.*}',
        cors_preflight=True,
    )
    config.add_view(
        cors_options_view,
        route_name='cors-options-preflight',
        permission=NO_PERMISSION_REQUIRED,
    )


def add_cors_to_response(event):
    request = event.request
    response = event.response
    if 'HTTP_ORIGIN' in request.headers.environ:
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Expose-Headers': 'Content-Type,Date,Content-Length,Authorization,X-Request-ID',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Accept-Language, Authorization ,X-Request-ID',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })


def cors_options_view(context, request):
    response = request.response
    if 'HTTP_ACCESS_CONTROL_REQUEST_HEADERS' in request.headers.environ:
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Expose-Headers': 'Content-Type,Date,Content-Length,Authorization,X-Request-ID',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Accept-Language, Authorization ,X-Request-ID',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })
    else:
        response.headers['HTTP_ACCESS_CONTROL_ALLOW_HEADERS'] = (
            'Origin,Content-Type,Accept,Accept-Language,Authorization,X-Request-ID')
    return response
