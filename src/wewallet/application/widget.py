from .plugins.jinja2.widget import SingleWidget as BaseSingleWidget
from .plugins.jinja2.widget import MultiWidget as BaseMultiWidget

from .requestable import Requestable


class SingleWidget(Requestable, BaseSingleWidget):
    pass


class MultiWidget(Requestable, BaseMultiWidget):
    pass
