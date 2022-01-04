# -*- coding: utf-8 -*-
"""
server1v6.py Program
Example of using server socket using Python
Using IPv6
Wait for connection on port 50000. Return time.
When connected, print out time on console
End with Ctrl+Break
Usage:　c:\>python server1v6.py
"""

# import modules
import socket
import datetime 

# Global variables
PORT = 50000      # Port number
HOST = ''

# Main
# Create socket
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# Set address
server.bind((HOST, PORT))
# Wait for connection
server.listen()

# Respond to the client
while True:                                    # Loop
    client, addr = server.accept()             # Get socket to send 
    msg = str(datetime.datetime.now())         # Create message
    client.sendall(msg.encode("utf-8"))        # Send message
    print(msg,"Got connection request!")
    print(client)
    client.close()                             # Close connection
# End server1v6.py