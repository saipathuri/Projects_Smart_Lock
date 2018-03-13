from peewee import *
import peeweeTestDatabase

db = SqliteDatabase('Addresses.db')
userdb = SqliteDatabase('SavedData.db')

#creating WhiteList and Users objects to put into db
class WhiteList(Model):
	name     		= CharField()
	macAddress		= CharField()

	class Meta:
			database = db

class Users(Model):
	username = CharField()
	password = CharField()

	class Meta:
			database = userdb

# creating database
def create_db_user():
	if not (db.table_exists(WhiteList)):
		print ("Creating table")
		db.create_tables([WhiteList])

	if not (userdb.table_exists(Users)):
		print ("Creating table")
		userdb.create_tables([Users])

#clear Users table
def clearUsers():
	print ("Clearing Users")
	cursor = userdb.cursor()
	cursor.execute('DELETE FROM Users')

#clear MAC table
def clearMAC():
	print ("Clearing MAC")
	cursor = db.cursor()
	cursor.execute('DELETE FROM WhiteList')

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

#add MAC into list of WhiteList
def addWhiteList(device, mac):
	newMAC = WhiteList(name = device, macAddress = mac)
	newMAC.save()

#delete MAC by MAC match
def deleteWhiteList(MAC):
	deleteMAC = WhiteList.get(WhiteList.macAddress == MAC)
	deleteMAC.delete_instance()
	print("Deleted " + MAC)

#see if a username exists
def findUser(name):
	user = Users.select().where(Users.username == name)
	print(user.exists)

#see if a MAC address exists
def findWhitelist(MAC):
	mac = WhiteList.select().where(WhiteList.macAddress == MAC)
	print(mac.exists)

#returns list of all WhiteListed Macs
def get_all_WhiteList():
	# db.connect()
	whitelist = []

	for adresses in WhiteList.select():
		whitelist.append(adresses)
	return whitelist

def retrieveUsers():
	#con = sql.connect("SavedData.db")
	cur = userdb.cursor()
	cur.execute("SELECT username, password FROM Users")
	users = cur.fetchall()
	#con.close()
	return users

if __name__ == '__main__':
	create_db_user()
	print("saved")