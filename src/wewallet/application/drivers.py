from wewallet.application.plugins.sqlalchemy.driver import DriverHolder
from wewallet.application.plugins.sqlalchemy.driver import driver

from wewallet.auth.driver import AuthDriver


class WeWalletDriverHolder(DriverHolder):

    @property
    @driver
    def auth(self):
        return AuthDriver()
