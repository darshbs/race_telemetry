import socket

# 0.0.0.0 means "Listen to EVERYTHING on this computer"
# This fixes issues where 'localhost' or '127.0.0.1' might be blocked.
UDP_IP = "0.0.0.0" 
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(1.0) 

print(f"RAW LISTENER: Waiting for ANY data on port {UDP_PORT}...")
print("If you don't see numbers below, it's a Firewall or Game Settings issue.")

try:
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            # Just print the length. If this prints, your connection works!
            print(f"Connection Successful! Received packet size: {len(data)}")
            
        except TimeoutError:
            pass
#comment
except KeyboardInterrupt:
    print("\nStopped.") 