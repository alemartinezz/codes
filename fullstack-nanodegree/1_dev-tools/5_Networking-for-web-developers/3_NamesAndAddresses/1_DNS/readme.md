# DNS

In essence, DNS is simply a database that links meaningful names (known as host names), such as http://www.microsoft.com, to a specific IP address, such as 192.168.124.1. Simply linking addresses to names is just the beginning, though, because DNS has many more features in addition to host-name-to-address mapping.

The key features of host name to IP mapping are as follows:

    Mappings of addresses to names and vice versa (known as records) are stored in a database.

    The DNS database is distributed.

    A DNS database also stores additional records.

Although DNS is a database, most importantly it’s a distributed database. Each DNS server contains only a small portion of the host name to IP address mappings (relative to the number of records for the entire Internet). Each DNS server is configured with a special record that tells the DNS server where (the IP address of another DNS server) it will perform a lookup for records it doesn’t have in its portion of the DNS database. Because of this arrangement, each DNS server maintains only a small portion of the total DNS host to IP address mappings. The collection of host-name-to-IP-address mappings contained with the DNS database is also known as a namespace. Essentially, when looking for a name in DNS, the DNS client first checks a top-level DNS server database. That server tells the client which DNS server hosts the next part of the DNS name, and the client then queries that server. This lookup-and-handoff process continues until the client finds the DNS server that hosts the DNS record in question, and that server provides the IP address.

In addition to the basic IP-address-to-host-name mapping records stored by the DNS database, records are also maintained by DNS for other purposes. DNS contains a number of record types that facilitate other applications. The Mail Exchanger (MX) record, for example, provides mail servers with the information required to forward e-mail messages to the recipient’s e-mail server. Another type of record, the service (SVC) record, is used by Microsoft Active Directory to locate network services.
Seeing the DNS difference

By itself, DNS doesn’t appear to do much, and on top of that, DNS can seem a bit intimidating because it has number of different features and record types. One key to understanding the importance of DNS is realizing how other processes and applications depend on the services DNS provides. By understanding how DNS provides the underlying services used by various applications, you can get a clearer picture of why DNS exists and how it works.

Many common applications use DNS services, including

    World Wide Web (WWW)

    E-mail

    Other applications, such as instant messaging

The World Wide Web depends on DNS for user-friendly navigation. You could get to a Web site by entering the IP address of a site in your Web browser, but remembering lots of arbitrary numbers isn’t easy for most folks. It’s much easier to remember a DNS name for a Web site that reflects its content, such as http://www.yahoo.com or http://www.microsoft.com. It’s fair to say that without DNS, the Web wouldn’t have become quite the phenomenon that it is now.
Serving the e-mail connection

E-mail is one of the more popular applications that use DNS. Although the Web simply uses DNS for linking names to IP addresses for Web sites, e-mail servers also require some specialized records above and beyond what is required for basic host name to IP addresses. For example, when an e-mail message is sent from your e-mail client (such as Microsoft Outlook or Netscape Messenger), it can be sent either directly to the target domain (Microsoft.com if the note was sent to user@microsoft.com) or to another e-mail server that is providing a relay service. If your e-mail application specifies an outgoing (SMTP) mail server that is not the final destination server for the message, you’re making use of the relay process.

An e-mail address is made up of two parts: a recipient and a host. In the address postmaster@domain.tld, postmaster is the recipient, the user who will receive the message. This is irrelevant to the SMTP process, though, because the mail transfer agent (MTA) is responsible for making sure that the message gets into the mailbox of the recipient.

The host, domain.tld, is of much more interest. In this case, domain.tld refers not to a host in the traditional sense of an A record but rather to a mail server known as a mail exchanger (MX). This server is responsible for accepting all mail for domain.tld, denoted by a special record — an MX record — in DNS.

Beyond the Web and e-mail are many applications that either rely on or can use DNS services. These applications can include databases, multi-tier Web applications built by using middleware or an application server, peer-to-peer sharing programs, instant messaging, and multiplayer games.