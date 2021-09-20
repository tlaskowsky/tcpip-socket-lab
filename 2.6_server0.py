# -*- coding: utf-8 -*-
"""
server0.py Program
Example of using server socket using Python
Wait for connection on port 50000. Return message.
Connect only once, then terminate connection.
Usage:　c:\>python server0.py
"""

# Import module
import socket

# Global variables
PORT = 50000        # Port number
HOST = ''
"""
"""

# Main
# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set address
server.bind((HOST, PORT))

# Wait for connection
server.listen()

# Respond to the client
client, addr = server.accept()                # Receive socket to accept
client.sendall(b"Hi, nice to meet you!\n") # Send message
client.close()                             # Close connection
server.close()                                # Close server port
# End server0.py
