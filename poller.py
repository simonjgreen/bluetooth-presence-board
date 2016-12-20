#!/usr/bin/python

import bluetooth
import time

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d bluetooth devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))

    service = DiscoveryService()
    devices = service.discover(2)

    for address, name in devices.items():
            print("BLE name: {}, address: {}".format(name, address))

    result = bluetooth.lookup_name('1C:66:AA:CF:DD:35', timeout=5)
    if (result != None):
        print "John: in"
    else:
        print "John: out"

    result = bluetooth.lookup_name('00:1D:D9:F9:79:43', timeout=5)
    if (result != None):
        print "Paul: in"
    else:
        print "Paul: out"

    time.sleep(60)
