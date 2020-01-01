#! /usr/bin/env python3.6

from netmiko import ConnectHandler

cisco_iosv1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.31',
    'username': 'admin',
    'password': 'cisco',
    #'port' : 8022,          # optional, defaults to 22
    #'secret': 'secret',     # optional, defaults to ''
}

cisco_iosv2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.32',
    'username': 'admin',
    'password': 'cisco',
    #'port' : 8022,          # optional, defaults to 22
    #'secret': 'secret',     # optional, defaults to ''
}

cisco_iosv3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.33',
    'username': 'admin',
    'password': 'cisco',
    #'port' : 8022,          # optional, defaults to 22
    #'secret': 'secret',     # optional, defaults to ''
}

#open a ssh-config-file with configuration lines
with open("ssh-config-file") as f:
    lines = f.read().splitlines()
    print (lines)

#create list of devices to configure here
device_list= [cisco_iosv2,cisco_iosv3]

#ssh to devices in the above list
for device in device_list:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)