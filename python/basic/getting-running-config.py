#! /usr/bin/env python3.6

import getpass
import telnetlib

#get the username and password for telnet session
user = input("Enter your username: ")
password = getpass.getpass()

#open the devices IPs from inventory file
inventorylist = open("inventory")

for line in inventorylist:
    print("Copying the Configs of " + line)
    HOST = line.strip() #remove extra spaces after reading IP address
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    #read the above output with below function
    readouput = tn.read_all()
    #create new file with write access(W)
    outputfile = open("running-config" + HOST, "wb")
    outputfile.write(readouput)
    outputfile.close