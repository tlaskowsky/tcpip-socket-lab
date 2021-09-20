# -*- coding: utf-8 -*-
"""
server1UDP.py Program
Example of using server socket using Pytho -- UDP
Wait at port 50000 and return current time
Print current time in the console
End with Ctrl+Break
Usage:　c:\>python server1UDP.py
"""

# Import module
import socket
import datetime 

# Global variable
PORT = 50000      # Port number
BUFSIZE = 4096    # Buffer size

# Main
# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to port
server.bind(("", PORT))

# Process client request
while True:                                    # Loop
    data, client = server.recvfrom(BUFSIZE)    # Get client socket 
    msg = str(datetime.datetime.now())         # Create message
    server.sendto(msg.encode("utf-8"), client) # Send message
    print(msg, "Got a connection!")
    print(client)
# End server1UDP.py
