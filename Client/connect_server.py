import socket
from tkinter import messagebox
import globals

def connect_to_server(ip):
    host = ip  # Replace with the server's IP address
    port = 12345  # Replace with the server's port number

    # Create a socket object
    globals.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        globals.client_socket.connect((host, port))
        messagebox.showinfo("Notification", "Kết nối đến server thành công")

        # Add your client logic here to send/receive data

    except socket.error as e:
        messagebox.showinfo("Error", "Lỗi kết nối đến server")