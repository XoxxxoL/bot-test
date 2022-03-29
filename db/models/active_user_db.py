from cgi import print_arguments
from pickletools import uint8
from db.base import Base

from sqlalchemy import Column, Integer, BigInteger, Date, ForeignKey


class ActiveUsers(Base):
    __tablename__ = 'user_active'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.telegram_id'))
    count_message = Column(Integer)
    date = Column(Date)