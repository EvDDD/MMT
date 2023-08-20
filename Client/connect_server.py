import socket

def connect_to_server():
    host = 'localhost'  # Replace with the server's IP address
    port = 12345  # Replace with the server's port number

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to server")

        # Add your client logic here to send/receive data

    except socket.error as e:
        print(f"Connection error: {str(e)}")

    finally:
        # Close the client socket
        client_socket.close()