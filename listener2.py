import socket
import csv
import time
from f1_2019_telemetry.packets import unpack_udp_packet

# Listen on all available interfaces
UDP_IP = "0.0.0.0"
UDP_PORT = 20777
FILENAME = "f1_2019_telemetry.csv"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# This line helps if another program recently used the port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(1.0) # Check for data every second

print(f"--- F1 2019 Logger Started ---")
print(f"Listening on Port: {UDP_PORT}")
print(f"Writing to: {FILENAME}")
print("ACTION: You must be driving on the track to see data!")

with open(FILENAME, mode='w', newline='', buffering=1) as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Speed", "Gear", "RPM", "Throttle", "Brake"])

    last_heartbeat = time.time()
    
    try:
        while True:
            try:
                data, addr = sock.recvfrom(2048)
                packet = unpack_udp_packet(data)

                if packet.header.packetId == 6:
                    p = packet.carTelemetryData[packet.header.playerCarIndex]
                    writer.writerow([packet.header.sessionTime, p.speed, p.gear, p.engineRPM, p.throttle, p.brake])
                    # Force write to disk
                    file.flush()
                    
                    print(f" [DATA] Time: {packet.header.sessionTime:.1f} | Speed: {p.speed} km/h  ", end='\r')

            except socket.timeout:
                # This runs if no data came in for 1 second
                if time.time() - last_heartbeat > 2:
                    print(f" [WAITING] Script is alive, but no game data... ({time.strftime('%H:%M:%S')})", end='\r')
                    last_heartbeat = time.time()

    except KeyboardInterrupt:
        print(f"\nStopped by user. Data saved to {FILENAME}")
    finally:
        sock.close()