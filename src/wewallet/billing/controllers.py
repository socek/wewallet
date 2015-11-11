from wewallet.application.controller import BaseController


class BillsController(BaseController):

    topmenu_highlight = 'bill:list'
    renderer = 'wewallet.billing:templates/bill/list.haml'

    def make(self):
        pass
