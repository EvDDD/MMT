import socket
import pickle
from PIL import Image

# Server configuration
HOST = 'localhost'
PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print('Connected to server:', HOST, PORT)

# Receive the serialized screenshot from the server
screenshot_data = b''
while True:
    data = client_socket.recv(4096)
    if not data:
        break
    screenshot_data += data

# Deserialize the screenshot object
screenshot = pickle.loads(screenshot_data)

# Save the screenshot as an image file
screenshot.save('screenshot.png')
print('Screenshot received and saved as screenshot.png')

# Close the connection
client_socket.close()
