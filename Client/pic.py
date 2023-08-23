import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from client import *
import socket
from connect_server import *
import pickle
from PIL import Image

screenshot = None

def open_pic_window(self):
    window = tk.Toplevel(self)
    window.title("Pic")
    window.geometry("140x74")

    window.butTake = tk.Button(window, text="Chụp", command=lambda:butTake_Click(window))
    window.butTake.place(x=12, y=12, width=50, height=50)

    window.button1 = tk.Button(window, text="Lưu", command=lambda:button1_Click(window))
    window.button1.place(x=80, y=12, width=50, height=50)

def butTake_Click(window):
    message = "pic"
    globals.client_socket.send(message.encode())
    screenshot_data = b''

    data = globals.client_socket.recv(8388608)
    screenshot_data += data

    # Deserialize the screenshot object
    global screenshot
    screenshot = pickle.loads(screenshot_data)
    

def button1_Click(window):
    # Add your code for saving the image here
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    # if file_path:
    #     messagebox.showinfo("Lưu", f"Lưu ảnh vào: {file_path}")
    screenshot.save(file_path)