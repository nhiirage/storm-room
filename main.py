from webapp2 import WSGIApplication
from webapp2_extras.routes import RedirectRoute
from handlers import static_handler
import ah_settings


app = WSGIApplication(
    [
        RedirectRoute(r'/', handler=static_handler.StaticHandler, name='static', strict_slash=True),
        RedirectRoute(r'/<page>/', handler=static_handler.StaticHandler, name='static', strict_slash=True),
    ],
    debug = ah_settings.debug
)

