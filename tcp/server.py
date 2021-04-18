# TCP server 

import socket
import threading

bind_ip = "10.10.10.10"
bind_port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)


print("████████╗ ██████╗ ██████╗     ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗")
print("╚══██╔══╝██╔════╝ ██╔══██╗    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗")
print("   ██║   ██║      ██████╔╝    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝")
print("   ██║   ██║      ██╔═══╝     ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print("   ██║    ╚██████╗██║         ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║")
print("   ╚═╝     ╚═════╝╚═╝         ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝")
print("")
print("")               
print("[*] Listening in %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):

 # Printing what client sends

 request = client_socket.recv(1024)

 print("[*] Received: %s" % request)

 client_socket.close()

while True:
 client,addr = server.accept()

 print("[*] Connection accepted from: %s:%d " % (addr[0],addr[1]))

 # We send to the client an answer for let him know that he connected successfully 

 client.send(bytes("[*] Se ha conectado correctamente", "utf-8"))

 client_handler = threading.Thread(target=handle_client,args=(client,))

 client_handler.start()
