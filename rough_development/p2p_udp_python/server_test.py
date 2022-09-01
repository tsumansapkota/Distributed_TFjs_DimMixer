# ----- An example UDP client in Python that uses recvfrom() method -----

import socket

import random

 

# Give price

def getPrice(corpName):

    if(corpName == "Example Corporation"):

        price = random.uniform(27.0, 29.0);

        return price;

    else:

        return "NA";

 

# Create an UDP based server socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

socket.bind(("127.0.0.1", 4141));

 

while(True):

    msgAndAddress = socket.recvfrom(1024);

    incName = msgAndAddress[0].decode();

    print(incName);

 

    price = getPrice(incName);

    print(price)

    priceStr = "%.2f"%price;

    socket.sendto(priceStr.encode(), msgAndAddress[1]);