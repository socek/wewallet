from wewallet.application.widget import SingleWidget


class UserWidget(SingleWidget):

    template = 'wewallet.home:templates/widgets/user.haml'

    def __init__(self, user):
        self.user = user

    def make(self):
        self.context['user'] = self.user
