from wewallet.application.controller import BaseController

from .widgets import UserWidget


class HomeController(BaseController):

    topmenu_highlight = 'home'
    renderer = 'wewallet.home:templates/index.haml'

    def make(self):
        self.context['x'] = 10
        users = self.context['users'] = []
        for user in self.drivers.auth.find_all():
            widget = UserWidget(user)
            widget.feed_request(self.request)
            users.append(widget)
