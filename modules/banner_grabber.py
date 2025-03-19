import socket

def banner_grabber(target):
    print(f"\n[+] Grabbing banners from {target}")
    try:
        s = socket.socket()
        s.connect((target, 80))
        s.send(b"HEAD / HTTP/1.1\r\nHost: %b\r\n\r\n" % target.encode())
        banner = s.recv(1024).decode()
        print(f"[BANNER] {banner}")
        s.close()
    except Exception as e:
        print(f"Error: {str(e)}")
