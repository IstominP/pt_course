from scapy.all import *

ap_list = []
def ssid(pkt) : 
	if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 8:
			if pkt.addr2 not in ap_list:
				ap_list.append(pkt.addr2)
				print("AP: %s SSID: %s" % (ptk.addr2, ptk.info))
				
sniff(iface='en0', prn=ssid)


# sendpfast(Ether(dst='18:31:bf:2c:f3:4c')/IP(dst='10.25.96.24')/ICMP('A'*100)*100, loop=1000)