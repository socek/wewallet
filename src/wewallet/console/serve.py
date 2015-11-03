from os.path import dirname

from bael.project.base import ProjectBase
from bael.project.develop import Develop
from bael.project.virtualenv import BaseVirtualenv
from baelfire.dependencies import AlwaysRebuild
from baelfire.dependencies import RunBefore
from baelfire.error import CommandAborted

import wewallet


class Project(ProjectBase):

    def phase_settings(self):
        super().phase_settings()
        self.paths['cwd'] = dirname(dirname(dirname(wewallet.__file__)))
        self.paths.set_path('package:src', 'cwd', 'src')
        self.paths.set_path('package:main', 'src', 'wewallet')
        self.paths.set_path('data', 'cwd', 'data')
        self.paths.set_path('report', 'data', 'report.yml')

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(Develop()))


class Serve(BaseVirtualenv):

    def phase_settings(self):
        super().phase_settings()
        self.paths.set_path('exe:pserve', 'virtualenv:bin', 'pserve')

    def create_dependecies(self):
        self.add_dependency(RunBefore(Project()))
        self.add_dependency(AlwaysRebuild())

    def build(self):
        try:
            self.popen(
                ['%(exe:pserve)s data/development.ini' % self.paths],
            )
        except CommandAborted:
            self.logger.info('Aborted')
