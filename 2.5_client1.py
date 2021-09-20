# -*- coding: utf-8 -*-
"""
client1.py Program
Example of using client socket using Python - UDP
Connect to server using port 50000
Once connected, send message to the server
Then display the message from the server
Usage　c:\>python client1.py
"""

# Import module
import socket
import sys

# Global variables
PORT = 50000       # Port number
BUFSIZE = 4096     # Buffer size

# Main
# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server
host = input("Connected server：")
try:
    client.connect((host, PORT))
except:
    print("Can not connect")
    sys.exit()
# Send message to the server
msg = input("Enter message: ")
client.sendall(msg.encode("utf-8"))
# Receive message from the server
data = client.recv(BUFSIZE)
print("Message from the server: ")
print(data.decode("UTF-8"))
# Close connection
client.close()                             
# End client1.py