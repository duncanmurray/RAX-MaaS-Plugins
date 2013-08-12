#!/usr/bin/python

import ping 
import sys
import re

## Playing with argparse instead
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("ip")
#args = parser.parse_args()
#print 'status', args.ip

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
ping_result = ping.do_one(target, 3, 32)

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

