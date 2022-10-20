#!/usr/bin/env python

import os
import time
from subprocess import check_output, STDOUT

os.system('vtysh -c "sh run" -c "config t" -c "router bgp 1000" -c "address-family ipv6 unicast" -c "network 2001:2022:3:3::/126" -c "do show run"')
#I prefer subprocess over os.system, but all the -c's and quotation weirdness - including having to remain in config t in order for the network commands to work -
#mandates its usage, along with the author's non-dev background. It isn't pretty, it's functinoal, and fucntional is pretty.


array = []
varhex = "00" # starting hex value
for i in range(0, 3):      # increment the addresses
    i = int(varhex, 16)     # define i as the decimal equivalent of varhex
    i +=4                   # increment i by one
    print("2001:2022:3:3::" + hex(i)[2:] + "128")  
    array.append("2001:2022:3:3::" + hex(i)[2:] + "/128");    # print out the incremented value, but in hex form
    varhex = hex(i)



for i in array:
    cmd = 'vtysh -c "sh run" -c "config t" -c "router bgp 1000" -c "address-family ipv6 unicast" -c "network {0}" -c "do show run"'.format(i)
    os.system(cmd)
    time.sleep(2)