from impaf.routing import Routing as BaseRouting


class Routing(BaseRouting):

    def make(self):
        super().make()
        self.read_from_dotted('wewallet.home:routing.yaml')
