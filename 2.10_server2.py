# -*- coding: utf-8 -*-
"""
server2.py Program
Example of using server socket using Python
Wait at port 50000 and return current time
After the client enters a message, return current time
When connected, print time to the console
End with Ctrl+Break
Usage　c:\>python server2.py
"""

# Import module
import socket
import datetime 

# Global variable
PORT = 50000      # Port number
BUFSIZE = 4096    # Buffer size

# Main
# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set address
server.bind(("",PORT))
# Wait for connection
server.listen()

# Process client request
while True:                                    # Loop
    client, addr = server.accept()             # Receive client socket
    msg = str(datetime.datetime.now())         # Create message
    print(msg,"Got a connection")
    print(client)
    data = client.recv(BUFSIZE)                # Receive message from colient 
    print(data.decode("UTF-8"))                # Output message
    client.sendall(msg.encode("utf-8"))        # Send message
    client.close()                             # Close connection
# End server2.py