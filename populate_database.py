# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Users, MenuItems, Transactions

engine = create_engine('sqlite:///librarydata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
sess = DBSession()

# Clear Database

sess.query(Transactions).delete()
sess.commit()
print "All Transactions cleared"
sess.query(MenuItems).delete()
sess.commit()
print "All MenuItems cleared"
sess.query(Users).delete()
sess.commit()
print "All Users cleared"


# Add users

# Admin User
Admin = Users(
	name = "Admin",
	admin = True,
	passcode = 1234)

sess.add(Admin)
sess.commit()

# Regular User
Standard = Users(
	name = "John Appleseed",
	admin = False,
	passcode = 4321)

sess.add(Standard)
sess.commit()


# Print all users
users = sess.query(Users).all()
print "The following users were added:"
for u in users:
	print u.name, "ID(" + str(u.id) + ")"

# Add menu items

Menu1 = MenuItems(
	name = "Burger",
	price = 10.50,
	description = "A Juicy patty in a squishy bun. Topped off with Lettuce, Tomato and Secret Sauce")

sess.add(Menu1)
sess.commit()

Menu2 = MenuItems(
	name = "Fries",
	price = 5.25,
	description = "The crispiest fries on earth. Salty and a touch of mmmh MSG")

sess.add(Menu2)
sess.commit()

Menu3 = MenuItems(
	name = "Coke",
	price = 1.50,
	description = "Bubbly and dark to quench your thirst")

sess.add(Menu3)
sess.commit()

Menu4 = MenuItems(
	name = "Nachos",
	price = 7.50,
	description = "Oh my crispy Tortilla chips, topped with Salsa, Guac and some Sour Cream")

sess.add(Menu4)
sess.commit()

Menu5 = MenuItems(
	name = "Chicken Fingers",
	price = 9.00,
	description = "Not real Chicken Fingers, but you will be licking yours")

sess.add(Menu5)
sess.commit()

# Print all menu items
items = sess.query(MenuItems).all()
print "The following Menu Items were added:"
for i in items:
	print i.name
	print i.description








