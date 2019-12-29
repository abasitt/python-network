#! /usr/bin/env python3.6

from netmiko import ConnectHandler

cisco_iosv = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.31',
    'username': 'admin',
    'password': 'cisco',
    #'port' : 8022,          # optional, defaults to 22
    #'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_iosv)


config_commands = ["interface loop1","ip add 1.1.1.1 255.255.255.0"]

output = net_connect.send_config_set(config_commands)

for n in range (21,31):
    print ("configuring vlan " + str(n) )
    config_commands = ["vlan " + str(n), "name pythonvlan_" + str(n)]
    output = net_connect.send_config_set(config_commands)

output = net_connect.send_command('show ip int brief')
print(output)

output = net_connect.send_command('show vlan brief')
print(output)