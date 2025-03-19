The Penetration Testing Toolkit is a modular Python-based tool designed for security assessments and ethical hacking. It includes multiple modules such as a Port Scanner, Brute-Forcer, Banner Grabber, and Directory Enumerator.

Port Scanner: Scans open ports on a target IP or URL using socket connections. Identifies active services and their corresponding ports.
Brute-Forcer: Attempts to crack login credentials by trying multiple passwords from a specified list. Uses HTTP POST requests to send login attempts.
Banner Grabber: Retrieves and displays service banners from open ports to identify the software and version running.
Directory Enumerator: Scans for hidden or sensitive directories on the target web server, helping identify possible attack vectors.
The toolkit leverages libraries such as requests, socket, and BeautifulSoup to interact with web servers and perform network operations. The modular design allows easy addition of new functionalities. The toolkit helps identify vulnerabilities like open ports, weak passwords, exposed banners, and hidden directories, assisting in penetration testing and security assessments.
