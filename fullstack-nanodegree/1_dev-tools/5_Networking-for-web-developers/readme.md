# Networking for web developers

`ping -c3 8.8.8.8`

`ip addr show eth0`

Display the ip address of the specified adapter.

`ip route show`

`ping -c3 8.8.8.8`

The server responded the ping 3 times.

`printf 'HEAD / HTTP/1.1\r\nHost: www.udacity.com\r\n\r\n' | nc www.udacity.com 80`

Wikipedia sent back the HTTP header.

`host -t aaaa google.com`

`host -t mx udacity.com`

`dig www.udacity.com`

`sudo tcpdump -n -c5 -i eth0 port 22`

`traceroute www.udacity.com`

`mtr www.udacity.com`