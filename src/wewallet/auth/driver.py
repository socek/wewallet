from wewallet.application.plugins.sqlalchemy.driver import ModelDriver

from .models import User


class AuthDriver(ModelDriver):
    model = User

    def get_by_email(self, email):
        return self.query(self.model).filter_by(email=email).first()

    def create(
        self,
        password=None,
        permissions=None,
        **kwargs
    ):
        obj = self.model()
        for key, value in kwargs.items():
            setattr(obj, key, value)

        if password:
            obj.set_password(password)

        permissions = permissions or []
        for perm in permissions:
            self.add_permission(obj, *perm)

        self.database().add(obj)
        return obj
