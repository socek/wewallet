from impaf.controller.json import JsonController


class HomeController(JsonController):

    # renderer = 'impex.home:templates/me.haml'

    def make(self):
        self.context['x'] = 10
