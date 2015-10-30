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
    'impaf==0.1',
]
dependency_links = [
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
        entry_points="""\
        [paste.app_factory]
            main = wewallet.application:application

        """,
    )
