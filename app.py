import scapy.layers.l2 as scapy


# ARP -  Address Resolution Protocol - mapping MC and IP
# 192.168.0.94 is ip
# 192.168.0.94/24 is whole subnet with the ip
target_ip = "192.168.0.94/24"

# pdst - Destination protocol address - ip for what we are asking for mac
# psrc - Source IP in the arp rq
# hwdst / hwsrc - destination / source MC
# ths is question who is this ip?
arp = scapy.ARP(pdst=target_ip)

# ethernet frames - pakets, so it is for creating the packets
# dst - destination MC, "ff:ff:ff:ff:ff:ff" is broadcast MC, special MC for broadcast to all devices, so it stands for all MC
# so this is broadcast
ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

# this is broadcast with question who is this ip
packet = ether / arp

# srp = send and receive packet
# timeout - wait for response
# verbose 0 - dont log info about the process
# function returns a tuple of two lists:
## The first list contains pairs of (packet sent, answer received).
## The second list contains packets that were sent but didn't receive any response.
# result = scapy.srp(packet, timeout=3, verbose=0)[0]
result = scapy.srp(packet, timeout=3, verbose=0)[0]

clients = []

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print('Available devices:\n')

for client in clients:
    print(f"1.    ip: {client['ip']}   mac: {client['mac']}")