import socket

def port_scanner(target):
    print(f"\n[+] Scanning ports on {target}")
    for port in range(1, 1025):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            s.close()
        except Exception as e:
            print(f"Error: {str(e)}")
