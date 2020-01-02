import json
from napalm import get_network_driver

device_list = ['192.168.122.31','192.168.122.32','192.168.122.33']


for device in device_list:
    driver = get_network_driver('ios')
    ios_sw = driver (device, 'admin', 'cisco')
    ios_sw.open()
    print ("Access " + str(device))
    ios_sw.load_merge_candidate(filename='ACL1.cfg')
    ios_sw.commit_config()
    ios_sw.close()