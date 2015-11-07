from wewallet.application.controller import BaseController


class HomeController(BaseController):

    renderer = 'wewallet.home:templates/index.haml'

    def make(self):
        self.context['x'] = 10
