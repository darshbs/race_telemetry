import socket
import struct

UDP_IP = "0.0.0.0" # Listen on all available interfaces
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(1.0) 

print("F1 2019 Listener Active. Drive out of the garage!")

# F1 2019 Car Telemetry format is slightly different than 2025
# It is 66 bytes per car (not 60) in the 2019 structure.
TELEMETRY_FORMAT = "<HfffBbHBBH4H4B4BH4f4B" 

try:
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            
            # F1 2019 Header is only 23 bytes!
            if len(data) >= 23:
                # In F1 2019, Packet ID is at index 5 (6th byte)
                packet_id = data[5]
                
                # Packet ID 6 is Car Telemetry
                if packet_id == 6:
                    # In F1 2019, the player index is usually 0 in Time Trial, 
                    # but we can read it from the header at index 3
                    player_index = data[3]
                    
                    # Header is 23 bytes. Each car telemetry block is 66 bytes.
                    offset = 23 + (player_index * 66)
                    
                    # Grab speed (km/h)
                    # The format for 2019 speed is usually the first value (u16)
                    speed = struct.unpack_from("<H", data, offset)[0]
                    
                    # Grab throttle (float) - Offset + 2 bytes
                    throttle = struct.unpack_from("<f", data, offset + 2)[0]
                    
                    # Grab steer (float) - Offset + 6 bytes
                    steer = struct.unpack_from("<f", data, offset + 6)[0]
                    
                    # Grab brake (float) - Offset + 10 bytes
                    brake = struct.unpack_from("<f", data, offset + 10)[0]

                    print(f"Speed: {speed} | Throttle: {throttle:.2f} | Brake: {brake:.2f}", end='\r')
            
        except TimeoutError:
            pass
#comment
except KeyboardInterrupt:
    print("\nStopped.")