from pyramid.security import Allow
from pyramid.security import Authenticated
from pyramid.security import Everyone


class SecureFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'edit'),
    ]

    def __init__(self, request):
        pass
