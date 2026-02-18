import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(1.0) 

print(f"Radio check! Listening for telemetry data on port {UDP_PORT}...")
print("Waiting for F1 25 to send data (Press Ctrl+C to stop).")

try:
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            
            # 1. UPDATED: F1 25 headers are 29 bytes long
            if len(data) >= 29:
                # 2. UPDATED: The Packet ID is now the 7th byte (index 6)
                packet_id = data[6]
                
                if packet_id == 0:
                    packet_type = "Motion Data"
                elif packet_id == 2:
                    packet_type = "Lap Data"
                elif packet_id == 6:
                    packet_type = "Car Telemetry (Speed, Throttle, Brake)"
                else:
                    packet_type = f"Other (ID: {packet_id})"
                
                print(f"Received: {packet_type}")
            
        except TimeoutError:
            pass
            
except KeyboardInterrupt:
    print("\nListener shut down cleanly.")