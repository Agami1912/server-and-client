import socket

HOST = '0.0.0.0'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print(f"you are now connected on server on adress {HOST}:{PORT}")

while True:
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))
    if not message or message.lower == "exit":
        print("you are Discconected")
        break

    print(f"client: {message}")
    reply = client_socket.recv(1024).decode('utf-8')
    print(f"server {reply}")

client_socket.close()
