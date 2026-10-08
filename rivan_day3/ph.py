import netmiko
from netmiko import ConnectHandler
import pprint as print
import json

### READ JSON FILE
with open('ph.json','r') as jfile:
    pfile = json.load(jfile)
    #print.pp(pfile)

#Connect to Netmiko
#DEVICE INFO
ph = {
    'device_type': 'cisco_ios',
    'host':'192.168.102.11',
    'username':'admin',
    'password': 'pass',
    'port':'22'
}

##COMMANDS##
config = [
    f'interface {pfile['config']['type']} {pfile['config']['id']}',
    f'ip add {pfile['config']['ipv4']['ip']} {pfile['config']['ipv4']['mask']}',
    f'description {pfile['config']['description']}',
    'end'
]
print.pp(config)


###Connect to DEVICE
## CTRL FORWARD SLASH - to become comment
cli = ConnectHandler(**ph)
cli.enable()

cli.send_config_set(config)

siib  = cli.send_command('show ip int br')
cli.disconnect()
print.pp(siib)