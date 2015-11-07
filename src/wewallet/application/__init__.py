from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from fanstatic import Fanstatic

from impaf.application import Application as BaseApplication

from .routing import Routing
from .security import SecureFactory


class Application(BaseApplication):

    class Config(BaseApplication.Config):
        routing_cls = Routing
        authorization_policy = ACLAuthorizationPolicy

    def _create_config(self):
        def create_jinja2_settings():
            self.settings['jinja2.extensions'] = [
                'hamlish_jinja.HamlishExtension',
            ]

        def add_debugtoolbar():
            if self.settings['debug']:
                self.config.include('pyramid_debugtoolbar')

        create_jinja2_settings()
        super()._create_config()
        add_debugtoolbar()
        self.config.include('pyramid_jinja2')

    def _generate_registry(self, registry):
        super()._generate_registry(registry)
        self.config.add_jinja2_renderer('.haml')

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


application = Application('wewallet')
