from os.path import dirname

from bael.project.base import ProjectBase
from bael.project.develop import Develop
from baelfire.dependencies import FileChanged
from baelfire.dependencies import RunBefore
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
        self.paths.set_path(
            'migrations',
            'cwd',
            'migrations',
        )
        self.paths.set_path(
            'versions',
            'migrations',
            'versions',
        )
        self.paths.set_path(
            'log_all',
            'data',
            'all.log',
        )
        self.paths.set_path('frontendini', 'data', 'frontend.ini')

    def generate_context(self):
        context = super().generate_context()
        context['alembic'] = {
            'script_location': self.paths['migrations'],
            'sqlalchemy.url': self.settings['db']['url'],
        }
        self.settings['loggers']['handler_all']['args'] = (
            self.settings['loggers']['handler_all']['args'] % self.paths
        )
        return context
