import socket

def scan_ports(host, start_port, end_port):
    """Scan a range of ports on a given host."""
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set timeout to 1 second
            s.settimeout(1)
            # Attempt to connect to host:port
            result = s.connect_ex((host, port))
            # Check if the connection was successful
            if result == 0:
                print(f"Port {port} is open")
            # Close the socket
            s.close()
        except socket.error:
            pass

# Usage example
host = 'scanme.nmap.org'
start_port = 1
end_port = 100
scan_ports(host, start_port, end_port)
