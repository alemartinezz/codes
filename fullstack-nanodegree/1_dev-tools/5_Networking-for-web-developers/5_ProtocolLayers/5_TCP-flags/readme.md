# TCP Flags

TCP Flags

Each TCP packet record that you look at in tcpdump has a section called Flags that appears right after the address and port information. It has one or more letters or dots inside square brackets:

19:51:58.304117 IP 10.20.27.153.59328 > 93.184.216.34.80: Flags [S], seq 2574797435, win 26883, options [mss 8961,sackOK,TS val 689168793 ecr 0,nop,wscale 7], length 0

Take a look at your tcpdump data again. You'll see different packets having flags such as [S], [S.], [.], [P.], and [F.].

The Flags field in tcpdump tells you which flags, or control bits, are set on each TCP packet.
What is a flag?

In low-level computer languages, a flag is a Boolean value — a true or false value — that is stored in memory as a single bit. If a flag bit is 1, we say the flag is set. If the flag bit is 0, the flag is cleared (or unset).

Usually, flags come in groups, each of which can be set or cleared.
The six basic TCP flags

The original TCP packet format has six flags. Two more optional flags have since been standardized, but they are much less important to the basic functioning of TCP. For each packet, tcpdump will show you which flags are set on that packet.

    SYN (synchronize) [S] — This packet is opening a new TCP session and contains a new initial sequence number.
    FIN (finish) [F] — This packet is used to close a TCP session normally. The sender is saying that they are finished sending, but they can still receive data from the other endpoint.
    PSH (push) [P] — This packet is the end of a chunk of application data, such as an HTTP request.
    RST (reset) [R] — This packet is a TCP error message; the sender has a problem and wants to reset (abandon) the session.
    ACK (acknowledge) [.] — This packet acknowledges that its sender has received data from the other endpoint. Almost every packet except the first SYN will have the ACK flag set.
    URG (urgent) [U] — This packet contains data that needs to be delivered to the application out-of-order. Not used in HTTP or most other current applications.

Three-way handshake

The first packet sent to initiate a TCP session always has the SYN flag set. This initial SYN packet is what a client sends to a server to start opening a TCP connection. This is the first packet you see in the sample tcpdump data, with Flags [S]. This packet also contains a new, randomized sequence number (seq in tcpdump output).

If the server accepts the connection, it sends a packet back that has the SYN and ACK flags, and acknowledges the initial SYN. This is the second packet in the sample data, with Flags [S.]. This contains a different initial sequence number.

(If the server doesn't want to accept the connection, it may not send anything at all. Or it may send a packet with the RST flag.)

Finally, the client acknowledges receiving the SYN|ACK packet by sending an ACK packet of its own.

This exchange of three packets is usually called the TCP three-way handshake. In addition to sequence numbers, the two endpoints also exchange other information used to set up the connection.
Four-way teardown

When either endpoint is done sending data into the connection, it can send a FIN packet to indicate that it is finished. The other endpoint will send an ACK to indicate that it has received the FIN.

In the example HTTP data, the client sends its FIN first, as soon as it is done sending the HTTP request. This is the first packet containing Flags [F.].

Eventually the other endpoint will be done sending as well, and will send a FIN of its own. Then the first endpoint will send an ACK.
In between

In a long-running connection, there will be many packets exchanged back and forth. Some of them will contain application data; others may be only acknowledgments with no data (length 0). However, all TCP packets in a connection except the initial SYN will contain an acknowledgment of all the data that the sender has received so far. Therefore, they will all have the ACK flag set. (This is why tcpdump depicts the ACK flag with just a dot: it's really common.)
ICMP and UDP don't have TCP flags

If you look at tcpdump data for pings or basic DNS lookups, you will not see flags. This is because ping uses ICMP, and basic DNS lookups use UDP. These protocols do not have TCP flags or sequence numbers.
