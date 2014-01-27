from webapp2 import WSGIApplication, Route
from handlers import home_handler

app = WSGIApplication(
    Route(r'/', handler=home_handler.HomeHandler, name='home'),
)

