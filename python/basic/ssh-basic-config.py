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

device_list= [cisco_iosv1,cisco_iosv2,cisco_iosv3]

for device in device_list:
    net_connect = ConnectHandler(**device)
    for n in range (21,24):
        print ("configuring vlan " + str(n) )
        config_commands = ["vlan " + str(n), "name pythonvlan_" + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)