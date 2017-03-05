import sys
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import String, DateTime, Boolean
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    ''' Class to represent Users
    '''
    __tablename__ = 'users'

    name = Column(
        String(250), nullable=False)
    id = Column(
        Integer, primary_key=True)
    admin = Column(
        Boolean, default=False, nullable=False)

    @property
    def serialize(self):
        return{
            'name'  :   self.name,
            'id'    :   self.id,
            'admin' :   self.admin
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
        Integer, nullable=False)
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
