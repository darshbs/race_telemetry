import socket

def debug_connection():
    # Use your ACTUAL IP here from ipconfig
    YOUR_IP = "0.0.0.0" 
    PORT = 20777
    
    print(f"--- HARDWARE DEBUG ---")
    print(f"Listening on: {YOUR_IP}:{PORT}")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((YOUR_IP, PORT))
        sock.settimeout(15) # Wait 15 seconds
        
        print("STATUS: Socket bound successfully. Waiting for game packets...")
        print("ACTION: Start driving on the track NOW.")
        
        data, addr = sock.recvfrom(2048)
        print(f"SUCCESS! Received {len(data)} bytes from {addr}")
        
    except PermissionError:
        print("ERROR: Windows is denying permission to use this port.")
    except OSError as e:
        print(f"ERROR: Port conflict? {e}")
    except socket.timeout:
        print("ERROR: Timeout. The game is simply NOT sending data to this IP.")
    finally:
        sock.close()

debug_connection()