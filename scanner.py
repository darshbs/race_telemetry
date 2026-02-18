import socket

def scan_for_game():
    # We create a socket that listens to EVERYTHING
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        sock.bind(("", 20777))
        sock.settimeout(15) # We will wait 15 seconds
        print("--- SCANNING FOR GAME TRAFFIC ---")
        print("1. Ensure F1 2019 is running.")
        print("2. Ensure you are actually DRIVING the car.")
        
        data, addr = sock.recvfrom(1024)
        print(f"\n[!!!] DATA DETECTED!")
        print(f"The game is sending data from: {addr}")
        print(f"Packet Size: {len(data)} bytes")
        return True
    except socket.timeout:
        print("\n[X] STILL FAILED: No traffic detected on Port 20777.")
        print("Check if F1 2019 > Telemetry Settings > UDP Telemetry is 'ON'.")
        return False
    finally:
        sock.close()

scan_for_game()

New-NetFirewallRule -DisplayName "F1 Telemetry Fix" -Direction Inbound -LocalPort 20777 -Protocol UDP -Action Allow