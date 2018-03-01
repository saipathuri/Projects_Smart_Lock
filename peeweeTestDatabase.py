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
	if not (db.table_exists(MACAddresses)):
		print "Creating table"
		db.create_tables([MACAddresses])

def get_all_Addresses():
	# db.connect()
	addrs = []

	for adresses in MACAddresses.select():
		#print('0')
		print(adresses.macAddress)
		addrs.append(adresses)
		#print(adresses)
	return addrs

def clearDB():
	print "Clearing DB"
	sql = 'DELETE FROM MACAddresses'
	#conn = db.connect('Addresses.db')
	cursor = db.cursor()

	cursor.execute('DELETE FROM MACAddresses')

def sendMacIntoDB():
	print "Inserting Mac Addresses into DB"
	addrs = find_macs.mac_addresses()
	for mac in addrs:
		first = MACAddresses(macAddress = mac)
		first.save()
	
if __name__ == '__main__':
	db.connect()
	create_db()
	clearDB()
	sendMacIntoDB()
	get_all_Addresses()
	db.close()