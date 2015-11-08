from .plugins.sqlalchemy.requestable import SqlalchemyRequestable
from .drivers import WeWalletDriverHolder


class Requestable(SqlalchemyRequestable):

    def generate_drivers(self):
        self.drivers = WeWalletDriverHolder(self.database)
