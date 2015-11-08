from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declarative_base


class Model(AbstractConcreteBase, declarative_base()):
    pass
