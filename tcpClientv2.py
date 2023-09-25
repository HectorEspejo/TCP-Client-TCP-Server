# ---- TCP CLIENT ------ #

# socket library for connecting

import socket

# User inputs host, port and message

host = input("Type IP address: ")

strPort = input("Type port: ")

# We will use 'google.com' as our target host

targetHost = host

targetPort = int(strPort)

# Creating socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # 'AF_INET' is for using standard IPv4 | 'SOCK_STREAM' indicates that this will be a TCP client

# Conncet to client

client.connect((targetHost, targetPort))

# Send data

client.send(b"Hey!")

# Receive data

response = client.recv(4096)

print (response)
