from common import template
import webapp2


class StaticHandler(webapp2.RequestHandler):
    def get(self, page="index"):
        View = template.Jinja("/templates/static/{0}.html".format(page))
        self.response.out.write(View.render())

