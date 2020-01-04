import json
from napalm import get_network_driver

#list of device IPs to config
device_list = ['192.168.122.31','192.168.122.32','192.168.122.33']

#loop to individual devices IP in the device list
for device in device_list:
    driver = get_network_driver('ios')
    ios_sw = driver (device, 'admin', 'cisco')       #use napalm driver to connect
    ios_sw.open()                                    #open the ssh connection
    print ("Accessing " + str(device))
    ios_sw.load_merge_candidate(filename='ACL1.cfg') #load the switch configuration and merge the ACL1.cfg file with it
    diff = ios_sw.compare_config()                   #compare the different of original and merge configuration
    if len(diff) > 0:
        print(diff)
        ios_sw.commit_config()
    else:
        print("No change required")
        ios_sw.discard_config()

    ios_sw.close()