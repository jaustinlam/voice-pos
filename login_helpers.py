from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, MenuItems, Transactions

engine = create_engine('sqlite:///librarydata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
sess = DBSession()

def getUserByPasscode(passcode):
	''' Finds a user by entered passcode

		Args:
			The passed in passcode
	'''
	try:
		user = sess.query(Users).filter_by(passcode=passcode).one()
		return user
	except:
		return None



