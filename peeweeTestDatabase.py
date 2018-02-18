from peewee import *

db = SqliteDatabase('Addresses.db')

# creating Object to hold send to database
class MACAddresses(Model):
		macAddress		= CharField()

		class Meta:
				database = db

# creating database
def create_db():
		db.connect()
		db.create_tables([MACAddresses])
		db.close()

def get_all_Addresses():
	#db.connect()
	addrs = []

	for adresses in MACAddresses.select():
		#print('0')
		print(adresses.macAddress)
		addrs.append(adresses)
		#print(adresses)

	for a in addrs:
		print(a)
		
	db.close()

	return addrs

#MACAddresses.delete().where(
#	(MACAddresses.macAddress == '202.212.292')).execute()

create_db()
first = MACAddresses(macAddress = "202.212.292")
print(first.save())
second = MACAddresses(macAddress = "201.209.222")
print(second.save())
get_all_Addresses()
db.close()


