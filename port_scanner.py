import socket
import sys

def scan(host, ports):
    print(f"[+] Scanning {host}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            pass

if __name__ == "__main__":
    target = input("Enter target IP/Host: ")
    ports = range(20, 1025)  # Common ports
    scan(target, ports)
