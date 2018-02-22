from peewee import *
import os
import subprocess
import find_macs


db = SqliteDatabase('Addresses.db')

# creating Object to hold send to database
class MACAddresses(Model):
		macAddress		= CharField()

		class Meta:
				database = db

# creating database
def create_db():
		db.connect()
		if not (db.table_exists(MACAddresses)):
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

def clearDB():
	sql = 'DELETE FROM MACAddresses'
	#conn = db.connect('Addresses.db')
	cursor = db.cursor()

	cursor.execute('DELETE FROM MACAddresses')





def sendMacIntoDB():

	for mac in find_macs.mac_addresses():
		first = MACAddresses(macAddress = mac)
		print(first.save())
	
create_db()
clearDB()
sendMacIntoDB()
get_all_Addresses()
db.close()


