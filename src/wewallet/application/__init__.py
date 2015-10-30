from impaf.application import Application as BaseApplication

from .routing import Routing


class Application(BaseApplication):
    _routing_cls = Routing

    def _create_config(self):
        super()._create_config()
        if self.settings['debug']:
            self.config.include('pyramid_debugtoolbar')


application = Application('wewallet')
