from wewallet.application.widget import SingleWidget


class MenuItemWidget(SingleWidget):

    template = 'wewallet.topmenu:templates/widgets/item.haml'

    def __init__(self, slug, label):
        self.slug = slug
        self.label = label

        self.args = []
        self.kwargs = {}

    def set_url_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def make(self):
        if self.slug:
            self.url = self.route_path(self.slug, *self.args, **self.kwargs)
        else:
            self.url = '#'

    def feed_request(self, parent):
        self.parent = parent
        super().feed_request(parent.request)

    def is_highlighted(self):
        return self.parent.highlight and self.parent.highlight == self.slug


class Menu(SingleWidget):
    template = 'wewallet.topmenu:templates/widgets/menu.haml'

    def __init__(self, highlight):
        self.items = []
        self.highlight = highlight

    def add_item(self, *args, **kwargs):
        obj = MenuItemWidget(*args, **kwargs)
        obj.feed_request(self)
        self.items.append(obj)

    def make(self):
        self.add_item(
            'home',
            'Główna',
        )
        self.add_item(
            'bill:list',
            'Rachunki',
        )
        self.add_item(None, 'Login')
        self.add_item(None, 'User')
