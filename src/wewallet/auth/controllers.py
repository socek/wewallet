from wewallet.application.controller import BaseController


class LoginController(BaseController):

    renderer = 'wewallet.auth:templates/login.haml'

    def make(self):
        self.context['x'] = 10
