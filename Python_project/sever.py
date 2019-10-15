import socket
#서버연결 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.1.1.3', 5000))
server_socket.listen(4)
client_socket, addr = server_socket.accept()
data = client_socket.recv(1024)
print(data)