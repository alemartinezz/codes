# Middleboxes 1: Firewalls & Filtering

Firewalls are devices that network operators can use to filter traffic that's coming into or leaving their network. A firewall is one example of a class of network devices called middleboxes — devices that inspect, modify, or filter network traffic. Other examples of middleboxes include intrusion detection systems and load balancers. Technically, it's only a middle-box if it's a separate device from the client or server — server-side "firewalls" like Linux iptables aren't middleboxes.

A firewall can be a real boon to an organization's network security. The most common configuration for a firewall is to drop any incoming traffic except traffic to (host, port) pairs that are supposed to be receiving connections from the Internet. This lets the network administrator be sure that other machines on the network — like backend databases or administrative systems — aren’t going to get direct attacks from outside.

But firewalls can cause trouble for application developers. If you're trying to test or deploy a network app and there's a firewall between your server and the user, that firewall can potentially interfere with your app or block it completely. In order to deploy an application on a particular server and port, it helps to know what kind of firewall might be between you and your user. One of the reasons that many non-Web applications use HTTP as a transport is that HTTP is often unblocked at firewalls even when other ports are blocked.

Aside from blocking traffic outright, middleboxes can also alter traffic, for instance replacing web pages with error messages. This is often done for social or political purposes. For instance, in the U.S., many schools use traffic filters of various sorts to prevent students from accessing web sites deemed inappropriate for children. But what sites get counted as "inappropriate" can reflect the biases or opinions of the people who wrote or configured the filter.

And people who program these things can always make mistakes, too. For instance, there's a whole class of bugs that arise from filters that try to block rude words, but end up blocking or replacing innocuous words that contain a rude word as a substring.

Rather famously, some countries have deployed large-scale firewalls or filters to censor their citizens' access to the global Internet. Major well-known sites such as YouTube and Twitter are sometimes blocked entirely in some countries. That can happen to your site, too — just something to keep in mind.
