from impaf.controller import Controller

from .widget import FormWidget


class FormskitController(Controller):

    def add_form(
        self,
        formcls,
        widgetcls=FormWidget,
        name='form',
        *args,
        **kwargs
    ):
        form = formcls(self.request, *args, **kwargs)
        widget = widgetcls(form)
        self.add_widget(name, widget)
        return form
