#!/usr/bin/python

import nmap
import sqlite3 as sql

def scan_mac():
    return_list = []
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sP')

    host_list = nm.all_hosts()
    for host in host_list:
        if 'mac' in nm[host]['addresses']:
            return_list.append(nm[host]['addresses']['mac'])

    return return_list

def clear_db():
    conn = sql.connect('test.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM scanned")

    conn.commit()
    conn.close()

def insert_scanned(lst):
    conn = sql.connect('test.db')
    c = conn.cursor()
    for i in lst:
        c.execute(""" INSERT INTO scanned (mac) VALUES (?)""", (i,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    while(True):
        lst = scan_mac()
        clear_db()
        insert_scanned(lst)

