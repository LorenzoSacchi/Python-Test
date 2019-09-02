#! /usr/local/bin/python3

import socket
import threading
import os

def handle_client(client_socket,addr):
    while True:
        try:
            request = client_socket.recv(4096).decode().rstrip()
            response = os.popen(request + ' 2>&1').read()
            output = response + addr[0] + ' >>> '
            client_socket.send(output.encode())
        except:
            break


def main():
    BIND_IP = '127.0.0.1'
    BIND_PORT = 9999
    IPV4 = socket.AF_INET
    TCP = socket.SOCK_STREAM


    server = socket.socket(IPV4, TCP)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)

    

    while True:
        client,addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client,addr))
        client_handler.start()
        client_handler.join()


if __name__ == "__main__":
    main()