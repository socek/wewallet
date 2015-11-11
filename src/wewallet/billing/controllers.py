from wewallet.application.controller import BaseController

from .widgets import BillList


class BillsController(BaseController):

    topmenu_highlight = 'bill:list'
    renderer = 'wewallet.billing:templates/bill/list.haml'

    def make(self):
        self.add_widget('list', BillList())
