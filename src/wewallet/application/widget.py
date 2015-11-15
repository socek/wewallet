from .plugins.formskit.widget import FormWidget
from .plugins.jinja2.widget import MultiWidget as BaseMultiWidget
from .plugins.jinja2.widget import SingleWidget as BaseSingleWidget

from .requestable import Requestable


class BaseFormWidget(object):

    def add_form(
        self,
        formcls,
        name='form',
        widgetcls=FormWidget,
        *args,
        **kwargs
    ):
        form = formcls(self.request, *args, **kwargs)
        widget = widgetcls(form)
        self.add_widget(name, widget)
        return form


class SingleWidget(
    Requestable,
    BaseSingleWidget,
    BaseFormWidget,
):
    pass


class MultiWidget(
    Requestable,
    BaseMultiWidget,
    BaseFormWidget,
):
    pass
