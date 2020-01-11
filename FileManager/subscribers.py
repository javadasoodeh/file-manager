# # subscribers.py
#
# import logging
#
#
# # calling after controller
# def callback(request, response):
#     # # create logger object
#     # logger = logging.getLogger('logger-object-name')
#     # # set default severity level
#     # logger.setLevel(logging.DEBUG)
#     # logger.addHandler(logging.StreamHandler())
#
#     if request.method == 'OPTIONS' and 'Origin' in request.headers and\
#             'Access-Control-Request-Method' in request.headers:
#         response.headers.update({
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Expose-Headers': 'Content-Type,Date,Content-Length,Authorization,X-Request-ID',
#             'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
#             'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
#             'Access-Control-Allow-Credentials': 'true',
#             'Access-Control-Max-Age': '1728000',
#         })
#
#
# def my_custom_subscriber(event):
#     event.request.add_response_callback(callback)
#
