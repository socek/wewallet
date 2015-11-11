from wewallet.application.controller import BaseController

from .widgets import BillList, CreateBillFormWidget


class BaseBillController(BaseController):
    topmenu_highlight = 'bill:list'


class BillsController(BaseBillController):

    renderer = 'wewallet.billing:templates/bill/list.haml'

    def make(self):
        self.add_widget('list', BillList())


class CreateBillController(BaseBillController):

    renderer = 'wewallet.billing:templates/bill/create.haml'

    def make(self):
        billing = self.drivers.billing.get_by_id(1)
        self.add_widget('form', CreateBillFormWidget(billing))
