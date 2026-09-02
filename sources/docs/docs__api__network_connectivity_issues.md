---
url: https://www.braze.com/docs/api/network_connectivity_issues
slug: docs__api__network_connectivity_issues
title: "API network connectivity issues"
description: "This reference article touches on API connectivity issues and how to troubleshoot them."
section: api/network_connectivity_issues
fetched: 2026-09-02
evidence: company-own (technical)
---
# API network connectivity issues

This reference article touches on API connectivity issues and how to troubleshoot them.

Braze API endpoints use a CDN that routes traffic to the closest POP based on DNS information. If you are having issues connecting or notice that you are connecting to a POP that is not efficient, make sure to use your provider’s DNS servers or DNS servers that are set up in the same data center as your server and have proper IP location meta-information associated with them.

We have noticed that a handful of firewalls attempt to modify or secure HTTPS/TLS traffic which interferes with connections to Braze API endpoints. If your servers are behind any sort of physical firewall, disable any HTTPS/TLS acceleration or modifications that the firewall or router is performing. Additionally, you can allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

Occasionally, iptables setups that filter on SYN/ACK/RST packets can also cause issues, so if you are using iptables on your host you could also allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

If you are still having network issues with connecting to Braze API endpoints, provide an MTR Test and the results from Fastly Debug while experiencing an issue and submit that with your support request. Note that the test results must be obtained from a server that is having issues connecting to Braze API endpoints, not from a development machine. A network capture (tcpdump or .pcap file) will also be helpful if it can be obtained.

For more information about MTR, check out these resources based on your operating system:

- GNU/Linux
 
- macOS

## Allowlisting Braze API endpoints IP ranges

To allowlist Braze API endpoints through your firewall, our CDN provides access to the list of assigned IP ranges through a JSON dump. For a list of Braze API IP ranges, refer to both Fastly’s public IP list and Cloudflare’s public IP list. Note that these IPs may change.

- 

New Stuff!
