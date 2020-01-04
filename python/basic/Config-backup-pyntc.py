import json
from pyntc import ntc_device as NTC

#list of device IPs to config
device_list = ['192.168.122.31','192.168.122.32','192.168.122.33']

#loop to individual devices IP in the device list
for device in device_list:
    sw_connect = NTC(host=device, username='admin', password= 'cisco', device_type='cisco_ios_ssh')
    sw_connect.open()
    ios_run = sw_connect.backup_running_config('backup' + str(device))