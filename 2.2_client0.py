# -*- coding: utf-8 -*-
"""
client0.py Program
Using client socket withPython
Example Connect to server using port 50000
Usage: c:\>python client0.py
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
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
client.connect((HOST, PORT))
# Receive message from server
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# Close socket
client.close()                             
# End client0.py