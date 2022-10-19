#!/usr/bin/env python

import os

subprocess.run("vtysh -c 'sh ipv6 route' -c 'config t' -c 'router bgp 1000' -c 'address-family ipv6 unicast' -c 'network 2001:50:50:50::/64' -c 'do show ipv6 route'")
#subprocess.run("vtysh -c 'config t'")
#subprocess.run("vtysh -c 'router bgp 1000'")
#subprocess.run("vtysh -c 'address-family ipv6 unicast'")
#subprocess.run("vtysh -c 'network 2001:2022:3:3::/64'")
#subprocess.run("vtysh -c 'show running-config'")
