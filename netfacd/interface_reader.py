#!/usr/bin/env python3

import netifaces
print(netifaces.interfaces())

"""
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adapter information')
"""

def iponly(interface):
    try:
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adapter information')

def maconly(interface2):
    try:
        print('MAC: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
    except:
        print('Could not collect adapter information')

def main():
    for i in netifaces.interfaces():
        iponly(i)
        print('\n****************')
        maconly(i)

main()
