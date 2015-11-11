from wewallet.application.plugins.sqlalchemy.driver import ModelDriver

from .models import Bill
from .models import Billing


class BillingDriver(ModelDriver):
    model = Billing


class BillDriver(ModelDriver):
    model = Bill
