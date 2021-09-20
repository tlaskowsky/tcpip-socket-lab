# -*- coding: utf-8 -*-
"""
client0udp.py Program
Example of using client socket using Python - UDP
Connect to server using port 50000
Usage　c:\>python client0udp.py
"""

# Import module
import socket

# Global variables
HOST = "localhost"  # Host name to connect
#HOST = "127.0.0.1" # Host IP to connect
PORT = 50000        # Port number
BUFSIZE = 4096      # Buffer size

# Main
# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send request to server
client.sendto(b"Hi!", (HOST, PORT))
# Receive answer from server
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# Close socket
client.close()                             
# End client0udp.py