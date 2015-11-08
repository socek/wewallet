# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'pyramid==1.5.7',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy==1.0.8',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms==2.0.2',
    'webhelpers2==2.0',
    'paginate==0.5',
    'paginate_sqlalchemy==0.2.0',
    'morfdict',
    'pyyaml',
    'impaf==0.1.1',
    'hamlish_jinja',
    'baelfire==0.3.1',
    'bael.project==0.2',
    'fanstatic',
    'js.jquery',
    'alembic',
    'psycopg2',
    'formskit',
]


def create_link(name, version):
    data = {
        'prefix': 'https://github.com/socek',
        'name': name,
        'version': version,
    }
    template = '%(prefix)s/%(name)s/tarball/master#egg=%(name)s-%(version)s'
    return template % data

dependency_links = [
    create_link('bael.project', '0.2'),
    create_link('baelfire', '0.3.1'),
    create_link('impaf', '0.1.1'),
]

if __name__ == '__main__':
    setup(
        name='WeWallet',
        version='0.1',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=install_requires,
        dependency_links=dependency_links,
        include_package_data=True,
        entry_points={
            'fanstatic.libraries': (
                'application = wewallet.application.resources:library',
            ),
            'console_scripts': (
                'wwcmd = wewallet.console.cmd:run',
            ),
            'paste.app_factory': (
                'main = wewallet.application:application',
            )
        }
    )
