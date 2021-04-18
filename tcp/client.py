# TCP client
import socket

target_host = "10.10.10.10"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start the connection

client.connect((socket.gethostname(), 80))

client.send(bytes("GET /HTTP/1.1\nHost: google.com", "utf-8"))

response = client.recv(1024)

print(response)
