def make_settings(settings, paths):
    project(settings, paths)
    database(settings, paths)
    # alembic(settings, paths)
    # fanstatic(settings, paths)
    debug(settings, paths)
    auth(settings, paths)


def database(settings, paths):
    # ----------------------------------------
    # This is example postgresql configuration
    # ----------------------------------------
    # settings['db']['type'] = 'postgresql'
    # settings['db']['login'] = 'develop'
    # settings['db']['password'] = 'develop'
    # settings['db']['host'] = 'localhost'
    # settings['db']['port'] = '5432'
    settings['db'] = {}
    settings['db']['type'] = 'sqlite'
    settings['db']['name'] = '%(project)s_develop'
    paths.set_path('sqlite_db', 'data', '%(db:name)s.db')


def project(settings, paths):
    paths.set_path('maindir', 'project', '../..')
    paths.set_path('data', 'maindir', 'data')

    paths.set_path('application', 'project', 'application')
    paths.set_path('routing', 'application', 'routing.yaml')


def alembic(settings, paths):
    paths['alembic'] = {
        'versions': ["%(maindir)s", 'migrations'],
        'ini': ["%(data)s", "alembic.ini"],
    }


def fanstatic(settings, paths):
    settings['fanstatic'] = {
        'bottom': True,
        'debug': True,
    }


def debug(settings, paths):
    settings['debug'] = True
    settings['pyramid.reload_templates'] = True
    settings['pyramid.debug_notfound'] = True
    settings['pyramid.debug_routematch'] = True


def auth(settings, paths):
    settings['auth_secret'] = 'changemeplz'
