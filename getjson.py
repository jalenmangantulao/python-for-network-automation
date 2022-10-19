import sys
from napalm import get_network_driver # import code from NAPALM
if len(sys.argv) != 2:
  print("You supplied ", len(sys.argv)-1, " arguments but 1 is needed")
  print("getjson.py requires: hostname")
  print("example: python3 getjson.py  sw-1")
  sys.exit()
hn = sys.argv[1]
driver = get_network_driver('eos')
device = driver(hn, 'admin', 'alta3')
device.open() # start the connection
print(device.get_config())

