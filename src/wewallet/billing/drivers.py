from wewallet.application.plugins.sqlalchemy.driver import ModelDriver

from .models import Bill
from .models import Billing


class BillingDriver(ModelDriver):
    model = Billing


class BillDriver(ModelDriver):
    model = Bill

    def find_by_billing(self, billing_id):
        return self.find_all().filter(Bill.billing_id == billing_id)
