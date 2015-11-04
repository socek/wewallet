from os.path import dirname

from bael.project.base import ProjectBase
from bael.project.develop import Develop
from bael.project.virtualenv import BaseVirtualenv
from baelfire.dependencies import AlwaysRebuild
from baelfire.dependencies import FileChanged
from baelfire.dependencies import RunBefore
from baelfire.error import CommandAborted
from baelfire.task import TemplateTask

import wewallet

from wewallet.application import application


class Project(ProjectBase):

    def phase_settings(self):
        application._generate_settings({}, endpoint='command')
        super().phase_settings()
        self.settings.update(application.settings)
        self.paths.update(application.paths)
        self.paths['cwd'] = dirname(dirname(dirname(wewallet.__file__)))
        self.paths.set_path('package:src', 'cwd', 'src')
        self.paths.set_path('package:main', 'src', 'wewallet')
        self.paths.set_path('package:console', 'package:main', 'console')
        self.paths.set_path(
            'package:wwtemplates',
            'package:console',
            'templates',
        )
        self.paths.set_path(
            'package:application',
            'package:main',
            'application',
        )
        self.paths.set_path(
            'package:settings',
            'package:application',
            'settings',
        )
        self.paths.set_path('data', 'cwd', 'data')
        self.paths.set_path('report', 'data', 'report.yml')

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(Develop()))


class IniTemplate(TemplateTask):

    source_name = 'template:ini'
    output_name = 'frontendini'

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(Project()))
        self.add_dependency(FileChanged('package:default'))
        self.add_dependency(FileChanged('package:local'))

    def phase_settings(self):
        super().phase_settings()
        self.paths.set_path(
            'template:ini',
            'package:wwtemplates',
            'frontendini.jinja2',
        )
        self.paths.set_path(
            'package:default',
            'package:settings',
            'default.py',
        )
        self.paths.set_path(
            'package:local',
            'package:settings',
            'local.py',
        )
        self.paths.set_path('frontendini', 'data', 'frontend.ini')


class Serve(BaseVirtualenv):

    def phase_settings(self):
        super().phase_settings()
        self.paths.set_path('exe:pserve', 'virtualenv:bin', 'pserve')

    def create_dependecies(self):
        self.add_dependency(RunBefore(IniTemplate()))
        self.add_dependency(AlwaysRebuild())

    def build(self):
        try:
            self.popen(
                ['%(exe:pserve)s %(frontendini)s --reload' % self.paths],
            )
        except CommandAborted:
            self.logger.info('Aborted')
