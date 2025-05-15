import socket
import datetime

def start_server(host: str, port: int):
    server_read = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_read.bind((host, port))
    print(f"Server started at {host}:{port}\n Listening now...")

    while True:
        # aguardando mensagem
        data, addr = server_read.recvfrom(1024)
        
        time = datetime.datetime.now().strftime('%H:%M:%S')
        message = data.decode('UTF-8').split(',')
        print(f'[{time}] [{message[0].upper()}]: {message[1]}')

if __name__=='__main__':

    HOST_WRITE = 'localhost'
    PORT_WRITE = 9000


    start_server(HOST_WRITE, PORT_WRITE)