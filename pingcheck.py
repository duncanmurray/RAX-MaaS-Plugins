#!/usr/bin/python

"""
This script can be used as a plugin for Rackspace Monitoring as a Service (MaaS)
It expects 1 argument which can be an IP or a FQDN. It will then send a ping to that target from the server the script is installed on and retun the time taken for the ping to be received. One use case would be to monitor internal networks such as a Rackspace RackConnected.
"""


import ping 
import sys
import re

## Playing with argparse instead
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("ip")
#args = parser.parse_args()
#print 'status', args.ip

ping_timeout = 3 # Seconds
packet_size = 32 # KB

# Check if argument was supplied
if len(sys.argv) > 1:
    # Define valid IP
    valid_ip = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", sys.argv[1])
    # Define valid FQDN
    valid_fqdn = re.match("(?=^.{1,254}$)(^(?:(?!\d|-)[a-zA-Z0-9\-]{1,63}(?<!-)\.?)+(?:[a-zA-Z]{2,})$)", sys.argv[1])
    # Check id valid IP or FQDN
    if not valid_ip or valid_fqdn:
        print 'status', 'supplied argument is an invalid IP or FQDN'   
        sys.exit(1) 
else:
    # Priint error message and exit
    print 'status', 'Please supply and IP or FQDN'
    sys.exit(1)

# Set target
target = sys.argv[1]
# Ping target
ping_result = ping.do_one(target, ping_timeout, packet_size)

# Check if we got a response
if not ping_result:
    # Exit if we got no response
    print 'status', target, 'is unreachable'
    sys.exit(1)
else:
    # If we got a response print the metrics
    print 'status', target, 'is alive'
    print 'metric', 'ping', 'double', '{0:g}'.format(ping_result)
    sys.exit(0)

