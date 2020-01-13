#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os, time

# arp scan terminal command
os.system("sudo arp-scan  --ignoredups -I wlan0 --localnet >>/path/to/your/log.txt/file")

# the time it takes to perform the scan in seconds
time.sleep(2)

person1 = "person1: ---"
person2 = "person2: ---"
person3 = "person3: ---"
person4 = "person4: ---"
person1_mac = "the address mac of the devices being checked"
person2_mac = ""
person3_mac = ""
person4_mac = ""

with open("/path/to/your/log.txt/file") as f:
    for line in f:
        if person1_mac in line:
            person1 = "person1: present"
        if person2_mac in line:
            person2 = "person2: present"
        if person3_mac in line:
            person3 = "person3: present"
        if person4_mac in line:
            person4 = "person4: present"

# removes file content
print(person1+"\n"+person2+"\n"+person3+"\n"+person4)
open('/path/to/your/log.txt/file', 'w').close()

