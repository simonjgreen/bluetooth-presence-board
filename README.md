# bluetooth-presence-board

requires:
- `sudo apt-get install python-bluez memcached python-memcache`

copy config.py.dist to config.py and insert your addresses

poller.py creates a presence.json which should be symlinked to your webroot along with the index.html. The jquery in the index.html pulls this JSON to update the page.
