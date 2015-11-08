from impaf.application import Application


class Jinja2Application(Application):

    def _create_config(self):
        self._create_jinja2_settings()
        super()._create_config()
        self.config.include('pyramid_jinja2')

    def _create_jinja2_settings(self):
        self.settings['jinja2.extensions'] = [
            'hamlish_jinja.HamlishExtension',
        ]

    def _generate_registry(self, registry):
        super()._generate_registry(registry)
        self.config.add_jinja2_renderer('.haml')
