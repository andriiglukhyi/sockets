import sys
import socket
socket.getaddrinfo('127.0.0.1', 3000)
infos = socket.getaddrinfo('127.0.0.1', 3000)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
with socket.socket(*stream_info[:3]) as client:

    client.connect(stream_info[-1])

    message = sys.argv[1:]
    message_to_server = ' '.join(message)

    client.sendall(message_to_server.encode('utf8'))
    buffer_length = 8

    message_complete = False

    message_back = ''

    while not message_complete:
        part = client.recv(1024)
        message_back += part.decode('utf8')
        if len(part) < buffer_length:
            break

    print(message_back)


