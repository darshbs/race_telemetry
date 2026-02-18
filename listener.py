import socket

# 1. Setup the address and port
UDP_IP = "127.0.0.1" # This IP means "my own local computer" (localhost)
UDP_PORT = 20777     # The default port F1 games use to broadcast telemetry

# 2. Create the socket (Think of this as building a digital mailbox)
# AF_INET tells Python to use standard IP addresses.
# SOCK_DGRAM tells Python to use UDP (which prioritizes speed over perfect delivery).
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. Bind the socket (Attaching the mailbox to our specific address and port)
sock.bind((UDP_IP, UDP_PORT))

# THE FIX: Tell the socket to timeout after 1 second
sock.settimeout(1.0)

print(f"Radio check! Listening for telemetry data on port {UDP_PORT}...")
print("Press Ctrl+C to stop.")

# 4. The Infinite Loop (Keep checking the mailbox)
try:
    while True:
        try:
        # sock.recvfrom waits until data arrives. 
        # 2048 is the "buffer size" (the maximum number of bytes to catch at once).
            data, addr = sock.recvfrom(2048)
        
        # Print a simple message showing we caught something
            print(f"Caught a packet! Size: {len(data)} bytes from {addr}")
            
        except TimeoutError:
            # SAFETY NET: If 1 second passes with no data, do not crash!
            # 'pass' simply tells Python to ignore the silence and loop back around.
            pass
        
except KeyboardInterrupt:
    # This cleanly stops the script if you press Ctrl+C
    print("\nListener shut down.")