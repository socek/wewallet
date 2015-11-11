from sqlalchemy.orm import sessionmaker

from impaf.requestable import Requestable
from impaf.utils import cached

from .driver import DriverHolder


class SqlalchemyRequestable(Requestable):

    def feed_request(self, request):
        super().feed_request(request)
        self.generate_drivers()

    @cached
    def database(self):
        connection = DatabaseConnection(self.settings, self.registry)
        return connection.database()

    def generate_drivers(self):
        self.drivers = DriverHolder(self.database)


class DatabaseConnection(object):

    def __init__(self, settings, registry):
        self.settings = settings
        self.registry = registry

    def database(self):
        if self.settings['db']['type'] == 'sqlite':
            return self._get_sqlite_database()
        else:
            return self._get_normal_database()

    def _get_sqlite_database(self):
        engine = self.registry['db_engine']
        return sessionmaker(bind=engine)()

    def _get_normal_database(self):
        db = self.registry['db']
        db.expire_all()
        return db
