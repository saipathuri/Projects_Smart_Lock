from flask import Flask, Response, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/insert', methods=['POST','GET'])
def insert():
   error = None
   if request.method == 'POST':
       if valid_insert(request.form['name'], request.form['mac']):
           insert_mac_name(request.form['name'], request.form['mac'])
           return "Success!"
       else:
           return "nah"


def valid_insert(name, mac):
    """
    This function determines if the name and mac address of a device are safe to
    be inserted into the db. Pretty basic right now

    Args:
        name (str): the name of the device
        mac  (str): the mac address of the device

    Returns:
        bool: True for valid/safe to insert, false for not
    """
    if type(name) == str and name.len() < 100:
        if type(mac) == str and mac.len() < 100:
            return True
    return False

def connect():
    """
    This function returns a connection to the databse

    Returns:
        sqlite3.Connection: connection to db
    """

    return sql.connect('test.db')

def create_db():
    """
    This function creates a table called devices
    """


    conn = connect()
    c = conn.cursor()

    c.execute("""CREATE TABLE devices 
                 (id INTEGER PRIMARY KEY, name varchar(25), mac varchar(30))""")

    conn.commit()
    conn.close()

def main():
    conn = connect()
    c = conn.cursor()

    #create_db()
    
def insert_mac_name(name, mac):
    """
    This function inserts the name and mac address of a device into the devices
    table of the db

    Args:
        name (str): the name of the device
        mac  (str): the mac address of the device
    """

    conn = connect()
    c = conn.cursor()

    c.execute("""INSERT INTO devices (name, mac) VALUES (?, ?)""", (name, mac))

    conn.commit()
    conn.close()


def get_macs():
    """
    This function returns all the mac addresses inside the table devices

    Returns:
        str[]: A list of all mac addresses inside the table devices
    """
 
    
    macs = []
    
    conn = connect()
    c = conn.cursor()

    for row in c.execute("""SELECT mac FROM devices"""):
        macs.append(row[0])
    
    conn.close()

    return macs
    
def match_macs(mac):
    """
    This function returns if the argument is in the table devices
    
    Args:
        mac(str): A mac address

    Returns:
        bool: if mac
    """

    return mac in get_macs()

if __name__ == "__main__":
    main()
    print(get_macs())
    print(match_macs("eyeyeyey"))
    print(match_macs("eyeyeyea"))
