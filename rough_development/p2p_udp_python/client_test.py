# ----- An example UDP client in Python that uses recvfrom() method -----

import socket

 

# Number of bytes to get

numBytes2Get = 1024;

 

# Create a UDP socket. UDP is datagram based.

destination         = ("127.0.0.1", 4141);

udpClientSocket     = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

 

# Send quote request

sentBytesCount      = udpClientSocket.sendto("Example Corporation".encode(), destination);

 

# Use receivefrom() to get quote

receivedBytes  = udpClientSocket.recvfrom(numBytes2Get);

 

# Print the quote

print(receivedBytes[0].decode());