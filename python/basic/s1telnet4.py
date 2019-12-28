#! /usr/bin/env python3.6

import getpass
import telnetlib


user = input("Enter your username: ")
password = getpass.getpass()

inventorylist = open('inventory')

for n in inventorylist:
	print("configure switch " + n)
	HOST = n
	tn = telnetlib.Telnet(HOST)

	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")

	tn.write(b"en\n")
	tn.write(b"cisco\n")
	tn.write(b"conf t\n")


	for n in range (5,15):
		vlan = "vlan " + str(n)
		name = "name Python_" + str(n)
		tn.write(vlan.encode('ascii') + b"\n")
		tn.write(name.encode('ascii') + b"\n")


	tn.write(b"end\n")
	tn.write(b"exit\n")

	print(tn.read_all().decode('ascii'))