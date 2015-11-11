from wewallet.application.plugins.sqlalchemy.driver import DriverHolder
from wewallet.application.plugins.sqlalchemy.driver import driver

from wewallet.auth.driver import AuthDriver
from wewallet.billing.drivers import BillDriver
from wewallet.billing.drivers import BillingDriver


class WeWalletDriverHolder(DriverHolder):

    @driver
    def auth(self):
        return AuthDriver()

    @driver
    def billing(self):
        return BillingDriver()

    @driver
    def bill(self):
        return BillDriver()
