def make_settings(settings, paths):
    project(settings, paths)
    database(settings, paths)
    debug(settings, paths)
    auth(settings, paths)
    logger(settings, paths)
    fanstatic(settings, paths)


def logger(settings, paths):
    settings['loggers'] = {
        'loggers': {
            'keys': 'root, sqlalchemy, alembic',
        },
        'handlers': {
            'keys': 'console, all',
        },
        'formatters': {
            'keys': 'generic',
        },
        'logger_root': {
            'level': 'INFO',
            'handlers': 'console, all',
        },
        'logger_sqlalchemy': {
            'level': 'INFO',
            'handlers': 'all',
            'qualname': 'sqlalchemy.engine',
            'propagate': '0',
        },
        'logger_alembic': {
            'level': 'INFO',
            'handlers': 'all',
            'qualname': 'alembic',
            'propagate': '0',
        },
        'handler_console': {
            'class': 'StreamHandler',
            'args': '(sys.stderr,)',
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'handler_all': {
            'class': 'FileHandler',
            'args': "('%%(log_all)s', 'a')",
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'formatter_generic': {
            'format': '%%(asctime)s %%(levelname)-5.5s [%%(name)s][%%(threadName)s] %%(message)s',
        },
    }


def database(settings, paths):
    # ----------------------------------------
    # This is example postgresql configuration
    # ----------------------------------------
    # settings['db']['type'] = 'postgresql'
    # settings['db']['login'] = 'develop'
    # settings['db']['password'] = 'develop'
    # settings['db']['host'] = 'localhost'
    # settings['db']['port'] = '5432'
    settings['db']['type'] = 'sqlite'
    settings['db']['name'] = '%(project)s_develop'
    paths.set_path('sqlite_db', 'data', '%(db:name)s.db')
    paths['db'] = settings['db']


def project(settings, paths):
    paths.set_path('maindir', 'project', '../..')
    paths.set_path('data', 'maindir', 'data')

    paths.set_path('application', 'project', 'application')
    paths.set_path('routing', 'application', 'routing.yaml')


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
