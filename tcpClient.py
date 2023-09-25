# ---- TCP CLIENT ------ #

# socket library for connecting

import socket

# We will use 'google.com' as our target host

targetHost = "0.0.0.0"

targetPort = 4444

# Creating socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # 'AF_INET' is for using standard IPv4 | 'SOCK_STREAM' indicates that this will be a TCP client

# Conncet to client

client.connect((targetHost, targetPort))

# Send data

client.send(b"Hi there!")

# Receive data

response = client.recv(4096)

print (response)
