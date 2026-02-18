import socket

# Bind to ALL interfaces
UDP_IP = "0.0.0.0" 
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# This command allows the port to be reused if it was stuck open
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    sock.bind((UDP_IP, UDP_PORT))
    print(f"LISTENING ON ALL IPS (0.0.0.0) PORT {UDP_PORT}")
    print("1. Make sure you are DRIVING (Time Trial), not in the menu.")
    print(f"2. Make sure Game Settings UDP IP is your PC IP (e.g., 192.168.x.x)")
    
    sock.settimeout(2.0)

    while True:
        try:
            data, addr = sock.recvfrom(4096)
            print(f"SUCCESS! Connected to {addr[0]} - Packet Size: {len(data)}")
        except TimeoutError:
            pass
            
except OSError as e:
    print(f"ERROR: {e}")
    print("This usually means another app (SimHub, CrewChief?) is already using Port 20777.")
except KeyboardInterrupt:
    print("\nStopped.")