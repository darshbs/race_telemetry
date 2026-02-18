import socket
from f1_2019_telemetry.packets import unpack_udp_packet

# Configure the socket
UDP_IP = "0.0.0.0" # Listen on all interfaces
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for F1 2019 telemetry on port {UDP_PORT}...")

try:
    while True:
        # Receive the raw binary data
        data, addr = sock.recvfrom(2048)
        
        # Unpack the packet into a Python object
        packet = unpack_udp_packet(data)
        
        # Packet ID 6 is Car Telemetry (Speed, Gear, RPM, etc.)
        if packet.header.packetId == 6:
            # Index 0 is usually the player's car
            player_car = packet.carTelemetryData[packet.header.playerCarIndex]
            
            speed = player_car.speed
            gear = player_car.gear
            revs = player_car.engineRPM
            
            print(f"Speed: {speed} km/h | Gear: {gear} | RPM: {revs}", end='\r')

except KeyboardInterrupt:
    print("\nStopping telemetry stream...")
finally:
    sock.close()