import socket
from datetime import datetime


def begining():
    print('--- Starting server on port {} at {} ---'.format(address[1], datetime.now()))


def end():
    print('--- Stopping server on port {} at {} ---'.format(address[1], datetime.now()))


with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP) as sock:

    address = ('127.0.0.1', 3000)
    sock.bind(address)
    begining()
    sock.listen(1)

    conn, addr = sock.accept()
    message_complete = False

    msg_from_client = ''

    while not message_complete:
        part = conn.recv(1024)
        msg_from_client += part.decode('utf8')
        if len(part) < 1024:
            break

    year_day = '2011/12/02'
    t = datetime.strptime(year_day, '%Y/%m/%d')
    print ('[{}] Echoed: {}'.format(t, msg_from_client))

    conn.sendall(msg_from_client.encode('utf8'))
    end()
    conn.close()
    sock.close()