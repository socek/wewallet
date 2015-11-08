from wewallet.application.plugins.formskit.widget import FormWidget


class LoginFormWidget(FormWidget):

    class Templates(FormWidget.Templates):
        password = 'wewallet.auth:/templates/forms/password.jinja2',
        text = 'wewallet.auth:/templates/forms/text.jinja2',
