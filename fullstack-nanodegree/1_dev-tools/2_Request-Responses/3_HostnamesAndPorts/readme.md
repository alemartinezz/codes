# Hostnames and Ports

## Hostnames

A full HTTP or HTTPS URI includes the hostname of the web server, like `www.udacity.com` or `www.un.int` or `www.cheeseboardcollective.coop` (my favorite pizza place in the world, in Berkeley CA). A hostname in a URI can also be an IP address: for instance, if you put http://216.58.194.174/ in your browser, you'll end up at Google.

> Why is it called a hostname? In network terminology, a host is a computer on the network; one that could host services.

The Internet tells computers apart by their **IP addresses**; every piece of network traffic on the Internet is labeled with the IP addresses of the sending and receiving computers. In order to connect to a web server such as `www.udacity.com`, a client needs to translate the hostname into an IP address. Your operating system's network configuration uses the Domain Name Service (DNS) — a set of servers maintained by Internet Service Providers (ISPs) and other network users — to look up hostnames and get back IP addresses.

In the terminal, you can use the **host** program to look up hostnames in DNS:

Some systems don't have the `host` command, but do have a similar command called `nslookup`. This command also displays the IP address for the hostname you give it; but it also shows the IP address of the DNS server that's giving it the answer:


IP addresses come in two different varieties: the older **IPv4** and the newer **IPv6**. When you see an address like `127.0.0.1` or `216.58.194.164`, those are IPv4 addresses. IPv6 addresses are much longer, such as `2607:f8b0:4005:804::2004`, although they can also be abbreviated.


## Localhost

The IPv4 address `127.0.0.1` and the IPv6 address `::1` are special addresses that mean "this computer itself" — for when a client (like your browser) is accessing a server on your own computer. The hostname `localhost` refers to these special addresses.

When you run the demo server, it prints a message saying that it's listening on `0.0.0.0`. This is not a regular IP address. Instead, it's a special code for "every IPv4 address on this computer". That includes the `localhost` address, but it also includes your computer's regular IP address.


## Ports

When you told your browser to connect to the demo server, you gave it the URI `http://localhost:8000/`. This URI has a port number of `8000`. But most of the web addresses you see in the wild don't have a port number on them. This is because the client usually figures out the port number from the URI scheme.

For instance, HTTP URIs imply a port number of `80`, whereas HTTPS URIs imply a port number of `443`. Your Python demo web server is running on port `8000`. Since this isn't the default port, you have to write the port number in URIs for it.

**What's a port number, anyway?** To get into that, we need to talk about how the Internet works. All of the network traffic that computers send and receive — everything from web requests, to login sessions, to file sharing — is split up into messages called **packets**. Each packet has the IP addresses of the computer that sent it, and the computer that receives it. And (with the exception of some low-level packets, such as ping) it also has the **port number** for the sender and recipient. IP addresses distinguish computers; port numbers distinguish programs on those computers.

We say that a server "listens on" a port, such as 80 or 8000. "Listening" means that when the server starts up, it tells its operating system that it wants to receive connections from clients on a particular port number. When a client (such as a web browser) "connects to" that port and sends a request, the operating system knows to forward that request to the server that's listening on that port.

> Why do we use port 8000 instead of 80 for the demo server? For historical reasons, operating systems only allow the administrator (or root) account to listen on ports below 1024. This is fine for production web servers, but it's not convenient for learning.
