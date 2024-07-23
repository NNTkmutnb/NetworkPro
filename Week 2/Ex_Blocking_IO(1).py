import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

#Blcoking
def create_blocking(host, ip):
    logging.info('Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Blocking - connecting')
    s.connect((host, ip))

    logging.info('Blocking - connected')
    logging.info('Blcoking - sending...')
    s.send(b'hello\r\n')

    logging.info('Blocking - waiting...')
    data = s.recv(1024)
    logging.info(f'Blocking - data = {len(data)}')
    logging.info('Blocking - closing')
    s.close()

def main():
    create_blocking('voidrealms.com', 80)

if __name__ == "__main__":
    main()