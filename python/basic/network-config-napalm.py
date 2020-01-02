import json

from napalm import get_network_driver

driver = get_network_driver('ios')
ios_sw = driver ('192.168.122.31', 'admin', 'cisco')
ios_sw.open()

ios_output = ios_sw.get_bgp_neighbors()
print (json.dumps(ios_output, indent=4))