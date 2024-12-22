import socket

HOST = '0.0.0.0'
PORT= 12345

server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

server_socket.listen(5)
print(f"server is listing {HOST}:{PORT}")

client_socket, client_adress = server_socket.accept()
print(f"client connected from adress: {client_adress}")

while True:
    message = client_socket.recv(1024).decode('utf-8')
    if not message or message.lower == "exit":
        print("client Discconected")
        break

    print(f"client: {message}")
    reply = input("You: ")
    client_socket.send(reply.encode('utf-8'))

client_socket.close()
server_socket.close()