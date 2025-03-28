import socket
import sys

def client_http(host, port):
    http_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_client.connect((host, int(port)))
    http_client.sendall(b'GET / HT TP/1.1\r\nHost: ' + host.encode() + b'\r\n\r\n')
    response = http_client.recv(4096)
    print(response.decode('utf-8'))
    http_client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 client.py <host> <port>")
    else:
        host = sys.argv[1]
        port = sys.argv[2]
        client_http(host, port)