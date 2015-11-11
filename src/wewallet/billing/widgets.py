from wewallet.application.widget import SingleWidget
from wewallet.utils.widgets import Link


class BillItemWidget(SingleWidget):

    template = 'wewallet.billing:templates/bill/widgets/item.haml'

    def __init__(self, item):
        self.item = item

    def make(self):
        self.context['item'] = self.item

    def feed_request(self, parent):
        self.parent = parent
        super().feed_request(parent.request)


class BillList(SingleWidget):
    template = 'wewallet.billing:templates/bill/widgets/list.haml'

    def __init__(self):
        self.items = []

    def add_item(self, *args, **kwargs):
        obj = BillItemWidget(*args, **kwargs)
        obj.feed_request(self)
        self.items.append(obj)

    def make(self):
        self.add_widget('link', Link())
        for bill in self.drivers.bill.find_by_billing(1):
            self.add_item(bill)
