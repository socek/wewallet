from impaf.controller import Controller


class HomeController(Controller):

    renderer = 'wewallet.home:templates/index.haml'

    def make(self):
        self.context['x'] = 10
