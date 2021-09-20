# -*- coding: utf-8 -*-
"""
gethostbyname.py Program
Convert host name to ip address
Usage　c:\>python gethostbyname.py
"""

# import module
import socket

# main threat
# loop
while True:
    try:
        hostname = input("Enter host name(End with q):")
        if hostname == "q":   # Done
            break
        print(socket.gethostbyname(hostname))
    except:                   # Error
        print("Could not convert")
# End of gethostbyname.py