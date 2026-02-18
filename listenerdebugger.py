import socket

# 0.0.0.0 tells Windows to listen on EVERY network card (Wi-Fi, Ethernet, etc.)
UDP_IP = "0.0.0.0" 
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # This allows multiple apps to potentially share the port (sometimes helps)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(10) # Wait 10 seconds
    
    print(f"Searching for F1 2019 on Port {UDP_PORT}...")
    print("ACTION REQUIRED: Go drive the car on track now!")

    data, addr = sock.recvfrom(2048)
    print(f"!!! DATA FOUND !!!")
    print(f"Source: {addr}")
    print(f"First 20 bytes of raw data: {data[:20].hex()}")

except socket.timeout:
    print("FAILED: Still nothing. This is almost certainly a Windows Firewall block.")
except Exception as e:
    print(f"ERROR: {e}")
finally:
    sock.close()