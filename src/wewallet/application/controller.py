from .plugins.formskit.controller import FormskitController
from .resources import Resources
from .requestable import Requestable

from wewallet.topmenu.widgets import Menu
from wewallet.utils.widgets import Link


class BaseController(
    FormskitController,
    Requestable,
):

    def _generate_resources(self):
        self.resources = Resources()

    def _create_context(self):
        super()._create_context()
        self._generate_resources()
        self.context['need'] = self.resources.need

    def _before_make(self):
        super()._before_make()
        self.add_widget(
            'topmenu',
            Menu(getattr(self, 'topmenu_highlight', None)),
        )
        self.add_widget(
            'link',
            Link(),
        )
