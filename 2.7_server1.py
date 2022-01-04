# -*- coding: utf-8 -*-
"""
server1.py Program
Example of using server socket using Python
Wait for connection on port 5000.  Return time.
When connected, print out time on console.
End with Ctrl+Break
Usage: c:\>python server1.py
"""

# Import modules
import socket
import datetime 

# Global variables
PORT = 50000      # Port Number
HOST = ''

# Main
# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set address
server.bind((HOST, PORT))
# Wait for connection
server.listen()

# Respond to the client
while True:                                    # Loop
    client, addr = server.accept()             # Get socket to send 
    msg = str(datetime.datetime.now())         # Create message
    client.sendall(msg.encode("UTF-8"))        # Send message
    print(msg, "Got connection request!")
    print(client)
    client.close()                             # Close the connection
# End server1.py