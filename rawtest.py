import socket

# We use 0.0.0.0 to catch data from any internal "door" Windows opens
UDP_IP = "0.0.0.0"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(5)

print("Starting RAW DATA test...")
print("Go drive the car NOW!")

try:
    data, addr = sock.recvfrom(2048)
    print(f"!!! SUCCESS !!! Received {len(data)} bytes from {addr}")
except socket.timeout:
    print("FAILED: The script heard absolutely nothing.")
finally:
    sock.close()