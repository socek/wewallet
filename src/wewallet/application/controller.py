from .plugins.formskit.controller import FormskitController
from .resources import Resources
from .requestable import Requestable


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
