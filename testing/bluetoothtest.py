from bluetooth import *
import PyOBEX
import sys


print ("performing inquiry...")

nearby_devices = discover_devices(lookup_names = True)

print ("found %d devices" % len(nearby_devices))

print(nearby_devices)

for name, addr in nearby_devices:
     print (" %s - %s" % (addr, name))


service_matches = find_service(address = '94:65:2D:7D:2D:98' )
if len(service_matches) == 0:
    print("Couldn't find the service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))
client = PyOBEX.client(host, port)
client.connect()
client.put("/home/pi/photobox/testing/test.txt", "Hello world\n")
client.disconnect()