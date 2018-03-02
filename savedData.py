from peewee import *

db = SqliteDatabase('SavedData.db')

#creating MACAddresses and Users objects to put into db
class MACAddresses(Model):
	macAddress		= CharField()

	class Meta:
			database = db

class Users(Model):
	username = CharField()
	password = CharField()

	class Meta:
			database = db

# creating database
def create_db():
	if not (db.table_exists(MACAddresses)):
		print ("Creating table")
		db.create_tables([MACAddresses])

	if not (db.table_exists(Users)):
		print ("Creating table")
		db.create_tables([Users])

#clear Users table
def clearUsers():
	print "Clearing Users"
	cursor = db.cursor()
	cursor.execute('DELETE FROM Users')

#clear MAC table
def clearMAC():
	print "Clearing MAC"
	cursor = db.cursor()
	cursor.execute('DELETE FROM MACAddresses')

# add user and password to Users table
def addUser(name, pas):
	newUser = Users(username = name, password = pas)
	newUser.save()

#delete user by name

#add MAC into list of saved
def addMAC(mac):
	newMAC = MACAddresses(macAddress = mac)
	newMAC.save()

#delete MAC by MAC match

#find a name
#find a MAC

