import socket
import csv
import os
from f1_2019_telemetry.packets import unpack_udp_packet

# --- Configuration ---
UDP_IP = "0.0.0.0"
UDP_PORT = 20777
FILENAME = "f1_2019_telemetry.csv"

# Define the CSV Header
HEADER = ["Timestamp", "Speed", "Gear", "RPM", "Throttle", "Brake"]

# Setup the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Recording to {FILENAME}. Press Ctrl+C to stop.")

# Open the file in append mode
with open(FILENAME, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(HEADER)  # Write the header first

    try:
        while True:
            data, addr = sock.recvfrom(2048)
            packet = unpack_udp_packet(data)

            # ID 6 is Car Telemetry
            if packet.header.packetId == 6:
                player_idx = packet.header.playerCarIndex
                player_data = packet.carTelemetryData[player_idx]

                # Prepare the row data
                # header.sessionTime is the time in seconds since the session started
                row = [
                    packet.header.sessionTime,
                    player_data.speed,
                    player_data.gear,
                    player_data.engineRPM,
                    player_data.throttle,
                    player_data.brake
                ]

                # Write to CSV
                writer.writerow(row)
                
                # Optional: print to console every few packets to see progress
                print(f"Captured: Time {packet.header.sessionTime:.2f}s | Speed {player_data.speed}", end='\r')

    except KeyboardInterrupt:
        print(f"\nRecording stopped. Data saved to {FILENAME}")
    finally:
        sock.close()