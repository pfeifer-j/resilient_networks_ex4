import socket
import hashlib

# ISS connection
server_name = "net1-public.informatik.uni-hamburg.de"
server_port = 23001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_name, server_port))
    print(f"Connected to {server_name}:{server_port}")

    # Receive data from the server
    data = client_socket.recv(1024)
    puzzle = data.decode()
    print(f"Received: {puzzle}")

    # Calculate matching hash
    def find_matching_hash():
        hashed_puzzle = hashlib.sha256(str(puzzle).encode('utf-8')).hexdigest()
        candidate = int(puzzle) + 1

        while True:
            hashed_candidate =  hashlib.sha256(str(candidate).encode('utf-8')).hexdigest()
            if hashed_candidate[:4] == hashed_puzzle[:4]:
                print(f"Hashed candidate: {hashed_candidate[:8]}")
                print(f"Hashed puzzle: {hashed_puzzle[:8]}")
                return candidate
            candidate = candidate + 1

    # Send our result
    result = find_matching_hash()
    client_socket.send(str(result).encode("utf-8"))
    print(f"Sent: {result}")

    # Recieve final answer from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

finally:
    # Close the socket
    client_socket.close()
    print("Connection closed")