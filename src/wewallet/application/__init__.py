from fanstatic import Fanstatic
from morfdict import StringDict
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from impaf.application import Application as BaseApplication
from .plugins.jinja2.application import Jinja2Application

from .routing import Routing
from .security import SecureFactory


class Application(
    Jinja2Application,
):

    class Config(BaseApplication.Config):
        routing_cls = Routing
        authorization_policy = ACLAuthorizationPolicy

    def _create_config(self):
        def add_debugtoolbar():
            if self.settings['debug']:
                self.config.include('pyramid_debugtoolbar')

        super()._create_config()
        add_debugtoolbar()

    def _generate_registry(self, registry):
        def sqlalchemy():
            engine = create_engine(self.settings['db:url'])
            registry['db_engine'] = engine
            registry['db'] = sessionmaker(bind=engine)()
        super()._generate_registry(registry)
        sqlalchemy()

    def _get_config_kwargs(self):
        def configure_authorization(data):
            data['authentication_policy'] = AuthTktAuthenticationPolicy(
                self.settings['auth_secret'],
                hashalg=self.settings.get('auth_hashalg', 'sha512'),
            )
            data['authorization_policy'] = self.Config.authorization_policy()
            data['root_factory'] = SecureFactory

        data = super()._get_config_kwargs()
        configure_authorization(data)
        return data

    def _return_wsgi_app(self):
        return Fanstatic(
            super()._return_wsgi_app(),
            **self.settings['fanstatic']
        )

    def _populte_default_settings(self):
        def morf_sql_url(obj, value):
            if obj['type'] == 'sqlite':
                value = 'sqlite:///%(paths:sqlite_db)s'
            else:
                value = (
                    '%(type)s://%(login)s:%(password)s@%(host)s:%(port)s/'
                    '%(name)s'
                )
            return value % obj

        super()._populte_default_settings()
        dbsettings = StringDict()
        dbsettings['url'] = ''
        dbsettings.set_morf('url', morf_sql_url)
        self.settings['db'] = dbsettings

application = Application('wewallet')
