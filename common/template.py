from jinja2 import Environment, FileSystemLoader
import ah_settings


class Jinja:
    def __init__(self, template):
        self.loader = Environment(loader=FileSystemLoader(ah_settings.app.get('path')))
        self.template = self.loader.get_template(template)

    def render(self, context={}):
        return self.template.render(context)