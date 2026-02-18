import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Using 127.0.0.1 specifically instead of 0.0.0.0
sock.bind(("127.0.0.1", 20777))
sock.settimeout(5) # Give up after 5 seconds of silence

print("Waiting for ANY data from the game...")

try:
    data, addr = sock.recvfrom(2048)
    print(f"SUCCESS! Received {len(data)} bytes from {addr}")
except socket.timeout:
    print("FAILED: No data received. The game isn't talking to this port.")
finally:
    sock.close()