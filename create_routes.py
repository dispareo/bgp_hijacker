#!/usr/bin/env python

import os

os.system("vtysh -c 'show running-config'")

os.system("vtysh -c 'router bgp 1000'")
os.system("vtysh -c 'address-family ipv6 unicast'")
os.system("vtysh -c 'network 2001:2022:3:3::/64'")
os.system("vtysh -c 'show running-config'")
