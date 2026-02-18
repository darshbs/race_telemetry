import socket
from f1_2019_telemetry.packets import unpack_udp_packet

# Using '' or '0.0.0.0' allows us to catch broadcasted data
UDP_IP = '' 
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This tells Windows to allow multiple 'listeners' and handle broadcast traffic
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(15)

print(f"Listening for BROADCAST data on port {UDP_PORT}...")
print("ACTION: Go drive on the track now!")

try:
    data, addr = sock.recvfrom(2048)
    print(f"!!! SUCCESS !!! Data caught from {addr}")
    
    packet = unpack_udp_packet(data)
    if packet.header.packetId == 6:
        print(f"Confirmed: Car Telemetry packet received.")
    else:
        print(f"Received Packet ID: {packet.header.packetId}")

except socket.timeout:
    print("FAILED: No broadcast data detected. Is your Ethernet set to 'Private'?")
except Exception as e:
    print(f"ERROR: {e}")
finally:
    sock.close()