from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from wewallet.application.models import Model


class Billing(Model):
    __tablename__ = 'billings'
    id = Column(Integer, primary_key=True)
    bills = relationship("Bill", backref="billing")


class Bill(Model):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True)
    billing_id = Column(Integer, ForeignKey('billings.id'))
    date = Column(Date(), nullable=False)
