from .plugins.sqlalchemy.requestable import SqlalchemyRequestable
from .plugins.beaker import BeakerRequestable
from .drivers import WeWalletDriverHolder


class Requestable(
    SqlalchemyRequestable,
    BeakerRequestable,
):

    def generate_drivers(self):
        self.drivers = WeWalletDriverHolder(self.database)

    def route_path(self, *args, **kwargs):
        return self.request.route_path(*args, **kwargs)
