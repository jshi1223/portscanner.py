import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Faster scanning
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            sock.close()
        except socket.error:
            print(f"❌ Could not connect to {target}")
            break

if __name__ == "__main__":
    target = input("Enter IP or Hostname to scan: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    
    try:
        target_ip = socket.gethostbyname(target)
        scan_ports(target_ip, start, end)
    except socket.gaierror:
        print("Invalid hostname or IP.")
