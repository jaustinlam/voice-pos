import sys
from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy import String, DateTime, Boolean
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    ''' Class to represent Users
    '''
    __tablename__ = 'users'

    id = Column(
        Integer, primary_key=True)
    name = Column(
        String(250), nullable=False)
    admin = Column(
        Boolean, default=False, nullable=False)
    passcode = Column(
        Integer, nullable=False, unique=True)

    @property
    def serialize(self):
        return{
            'id'    :   self.id,
            'name'  :   self.name,
            'admin' :   self.admin,
            'passcode'  :   self.passcode
        }

class MenuItems(Base):
    ''' Class to represent items on the menu
    '''
    __tablename__ = 'menuitems'

    name = Column(
        String(250), nullable=False)
    id = Column(
        Integer, primary_key=True)
    price = Column(
        Float, nullable=False)
    description = Column(
        String(1000))


    @property
    def serialize(self):
        return{
            'name'  :   self.name,
            'id'    :   self.id,
            'price' :   self.price,
            'description' : self.description
        }

class Transactions(Base):
    ''' Records of Transactions
    '''
    __tablename__ = 'transactions'

    id = Column(
        Integer, primary_key=True)
    menu_id = Column(
        Integer, ForeignKey('menuitems.id'), nullable=False)
    user_id = Column(
        Integer, ForeignKey('users.id'), nullable=False)
    date = Column(
        DateTime)
    menuitems = relationship('MenuItems')
    users = relationship('Users')

    @property
    def serialize(self):
        return {
            'id'        :   self.id,
            'menu_id'   :   self.menu_id,
            'user_id'   :   self.user_id,
            'date'      :   self.date,
        }




engine = create_engine(
    'sqlite:///librarydata.db')
Base.metadata.create_all(engine)
