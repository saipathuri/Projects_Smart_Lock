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
	print ("Clearing Users")
	cursor = db.cursor()
	cursor.execute('DELETE FROM Users')

#clear MAC table
def clearMAC():
	print ("Clearing MAC")
	cursor = db.cursor()
	cursor.execute('DELETE FROM MACAddresses')

# add user and password to Users table
def addUser(name, pas):
	newUser = Users(username = name, password = pas)
	newUser.save()
	print("Added " + name)

#delete user by name
def deleteUser(name):
	deleteUser = Users.get(Users.username == name)
	deleteUser.delete_instance()
	print("Deleted " + name)

#add MAC into list of saved
def addMAC(mac):
	newMAC = MACAddresses(macAddress = mac)
	newMAC.save()

#delete MAC by MAC match
def deleteMAC(MAC):
	deleteMAC = MACAddresses.get(MACAddresses.macAddress == MAC)
	deleteMAC.delete_instance()
	print("Deleted " + MAC)

#see if a username exists
def findUser(name):
	user = Users.select().where(Users.username == name)
	print(user.exists)

#see if a MAC address exists
def findMAC(MAC):
	mac = MACAddresses.select().where(MACAddresses.macAddress == MAC)
	print(mac.exists)


addUser("John", "abcd")
findUser("John")
deleteUser("John")