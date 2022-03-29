from email.policy import default
from db.base import Base

from sqlalchemy import Column, Integer, TEXT
from sqlalchemy_utils.types.choice import ChoiceType

from misc.vriables import MONEY_TYPES


class Business(Base):
    __tablename__ = 'business'
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(TEXT)
    price = Column(Integer)
    profit = Column(Integer)
    money_type = Column(ChoiceType(MONEY_TYPES), default='money')
    
    def __repr__(self) -> str:
        return self.name