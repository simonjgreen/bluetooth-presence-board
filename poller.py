#!/usr/bin/python

import bluetooth
import time
import memcache
import json
from config import peeps

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    
    presencearray = []
    for peep, mac in peeps.items():
        result = bluetooth.lookup_name(mac, timeout=5)
        if (result != None):
            print peep + ": detected"
            try:
                mc.set(peep, "present", time=60)
            except:
                print "Write failed for " + peep

        try:
            presence = mc.get(peep)
            print peep + " " + presence + " in memcached"
            presencearray.append(peep)

        except:
            print "Get failed for " + peep

    with open('presence.json', 'w') as output:
        json.dump({"results": presencearray}, output)
