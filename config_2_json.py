from napalm import get_network_driver
import json
driver = get_network_driver('eos')
device = driver('sw-1', 'admin', 'alta3')
device.open() # start the connection
config = device.get_config()
print("UGLY JSON-LIKE BLOB:\r" )
print(device.get_config())
print("REAL JSON:\r" )    
print(json.dumps( config ,indent=4, separators=(',', ': ')))

