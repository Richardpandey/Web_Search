# ports.py
import socket
from urllib.parse import urlparse

def run(url, log=print):
    log("[*] Starting Port Scan...")

    # Extract host automatically from URL
    parsed = urlparse(url)
    host = parsed.hostname

    if not host:
        log("[!] Could not parse host from URL.")
        return

    # List of common ports to scan
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]
    open_ports = []

    for port in ports_to_scan:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((host, port)) == 0:
                log(f"[OPEN] Port {port}")
                open_ports.append(port)
            s.close()
        except:
            pass

    if not open_ports:
        log("[*] No common ports open.")

    log("[*] Port Scan Completed.\n")
