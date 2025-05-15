import socket
import json

def start_server(host_read: str, port_read: int, host_write: str, port_write: int):
    server_read = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_read.bind((host_read, port_read))
    print(f"Server started at {host_read}:{port_read}\n Listening now...")

    server_write = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # aguardando mensagem
        data, addr = server_read.recvfrom(1024)
        message = data.decode('UTF-8').split(',')
        
        data_client = f'{message[0]}, {message[1]}, {addr}'.encode('UTF-8')
        #print(data_client)
        
        # enviando mensagem para server_read
        server_write.sendto(data_client, (host_write, port_write))

if __name__=='__main__':

    HOST_READ = 'localhost'
    PORT_READ = 8000

    HOST_WRITE = 'localhost'
    PORT_WRITE = 9000


    start_server(HOST_READ, PORT_READ, HOST_WRITE, PORT_WRITE)