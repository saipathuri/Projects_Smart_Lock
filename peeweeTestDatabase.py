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
	db.connect()
	addrs = []

	for adresses in MACAddresses.select():
		addrs.append(adresses)
		print(adresses)

	db.close()

	return addrs

create_db()
first = MACAddresses(macAddress = '202.212.292')
first.save()
get_all_Addresses()

db.close()



