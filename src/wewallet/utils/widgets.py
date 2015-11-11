from wewallet.application.widget import SingleWidget


class Link(SingleWidget):
    template = 'wewallet.utils:templates/widgets/link.haml'
    _default_classes = ['btn']

    def make(self, slug, label, *args, cls=['btn-primary'], **kwargs):
        self.context['classes'] = ' '.join(self._default_classes + cls)
        self.context['href'] = self.route_path(slug, *args, **kwargs)
        self.context['label'] = label
