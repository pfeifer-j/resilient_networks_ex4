import socket
import hashlib
import random

# ISS connection
server_ip = "net1-public.informatik.uni-hamburg.de"
server_port = 23001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to {server_ip}:{server_port}")

    # Send data to the server
    message = "I need a puzzle!"
    client_socket.sendall(message.encode())
    print(f"Sent: {message}")

    # Receive data from the server
    data = client_socket.recv(1024)
    puzzle = data.decode()
    print(f"Received: {puzzle}")

    # Calculate matching hash
    def find_matching_hash():
        hashed_puzzle = hashlib.sha256(str(puzzle).encode('utf-8')).hexdigest()
        while True:

            candidate = random.Random().randint(0,1000000)
            if candidate == puzzle:
                continue
            hashed_candidate =  hashlib.sha256(str(candidate).encode('utf-8')).hexdigest()

            if hashed_candidate[:4] == hashed_puzzle[:4]:
                print("Matching hash found!")
                print(f"Hashed candidate: {hashed_candidate[:]}")
                print(f"Hashed puzzle: {hashed_puzzle[:]}")

                return candidate

    # Send our result
    result = find_matching_hash()
    client_socket.sendall(str(result).encode())
    print(f"Sent: {str(result)}")

    # Recieve final answer from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

finally:
    # Close the socket
    client_socket.close()
    print("Connection closed")