import socket
import pyautogui
import pickle

# Server configuration
HOST = 'localhost'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening on {}:{}'.format(HOST, PORT))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Connected to client:', client_address)

# Capture a screenshot
screenshot = pyautogui.screenshot()

# Serialize the screenshot object
screenshot_data = pickle.dumps(screenshot)

# Send the serialized screenshot to the client
client_socket.sendall(screenshot_data)

# Close the connection
client_socket.close()
server_socket.close()
