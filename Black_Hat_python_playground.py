import socket

target_host = "127.0.01"
target_port = 80

#Create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Connect to the client

#client.sendto((target_host,target_port))

#send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

#Receive some data
respone = client.recv(4096)

print(data.decode())
client.close()
