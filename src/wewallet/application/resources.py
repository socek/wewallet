from fanstatic import Library
from fanstatic import Resource

from wewallet.fanstatic import Resources as BaseResources

library = Library('application', 'static')

bootstrap = Resource(library, 'css/bootstrap.css', bottom=False)
main = Resource(library, 'css/main.css', bottom=False)
login = Resource(library, 'css/login.css', bottom=False)
table = Resource(library, 'css/table.css', bottom=False)
register = Resource(library, 'css/register.css', bottom=False)
flexslider = Resource(library, 'css/flexslider.css', bottom=False)
fontstyle = Resource(library, 'css/font-style.css', bottom=False)


class Resources(BaseResources):

    def __init__(self):
        super().__init__()
        self.add_resource('bootstrap', bootstrap)
        self.add_resource('main', main)
        self.add_resource('login', login)
        self.add_resource('table', table)
        self.add_resource('register', register)
        self.add_resource('flexslider', flexslider)
        self.add_resource('fontstyle', fontstyle)
