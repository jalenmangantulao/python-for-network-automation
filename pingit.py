#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Writing a script to perform ICMP checks."""

import os
import argparse

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def main():
    # switchlist = ["172.0.1.2", "sw-1", "sw-2", "8.8.8.8"]   # CUSTOMIZE THIS LIST WITH IPs to PING
    # switchlist = []
    # switchlist = input('Provide IPs to ping separated by commas: ').split(',')
    
    # challenge 01
    #parser.add_argument('--nargs', nargs='+') 

    switchlist = args.ip

    ## Use a loop to check each device for ICMP responses
    print("\n***** STARTING ICMP CHECKING *****")
    for x in switchlist:
        if ping_router(x):
            print(f"IP address {x} is responding to ICMP\n")
        else:
            print(f"IP address {x} is not responding to ICMP\n")

if __name__ == "__main__":
    # python3 pingit.py --ip <ip address>
    #challenge 01
    parser = argparse.ArgumentParser(description='A simple ICMP checker')

    parser.add_argument('-i', '--ip', nargs='+', help='space delimited hosts to ping')
    args = parser.parse_args()
    main()
