import json

from napalm import get_network_driver

device_list = [['192.168.122.31','192.168.122.32','192.168.122.33']]


for device in device_list:
    driver = get_network_driver('ios')
    ios_sw = driver (device, 'admin', 'cisco')
    ios_sw.open()
    ios_output = ios_sw.get_bgp_neighbors()
    print (json.dumps(ios_output, indent=4))
    ios_sw.close()