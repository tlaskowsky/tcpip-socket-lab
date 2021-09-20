# -*- coding: utf-8 -*-
"""
server3.py Program
Example of using server socket using Python
Wait at port 50000 and return current time
After the client enters a message, return current time
When connected, print time to the console
Use threads to perform parallel processing
End with Ctrl+Break
Usage　c:\>python server3.py
"""

# Import module
import socket
import datetime 
import threading

# Global variable
PORT = 50000     # Port number
BUFSIZE = 4096   # Buffer size

# Start client handler
#client_handler() function
def client_handler(client, clientno, msg):
    """
    Thread to process client request
    """
    data = client.recv(BUFSIZE)          # Receive from client 
    print("(", clientno, ")",           
          data.decode("UTF-8"))          # Output received message
    client.sendall(msg.encode("utf-8"))  # Send message
    client.close()                       # Close connection
#client_handler() End

# Main
# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set address
server.bind(("", PORT))
# Wait for connection
server.listen()
#　Initialize client number
clientno = 0

# Process client request
while True:                                 # Loop
    client, addr = server.accept()          # Receive socket info
    clientno += 1                           # Increment client number 
    msg = str(datetime.datetime.now())      # Create message
    print(msg,"Got a connection (",clientno,")")
    print(client)
    # Setup thread and initialize
    p = threading.Thread(target = client_handler,
                         args = (client, clientno, msg))
    p.start()  
# End server3.pyの