import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from client import *
import socket
from connect_server import *

def open_pic_window(self):
    window = tk.Toplevel(self)
    window.title("Pic")

    window.picture = tk.PhotoImage()
    window.butTake = tk.Button(window, text="Chụp", command=lambda:butTake_Click(window))
    window.button1 = tk.Button(window, text="Lưu", command=lambda:button1_Click(window))

    window.picture_label = tk.Label(window, image=window.picture)
    window.picture_label.pack()

    window.butTake.pack(side=tk.LEFT)
    window.button1.pack(side=tk.LEFT)

def butTake_Click(window):
    message = "Hello, server!"
    globals.client_socket.send(message.encode())

def button1_Click(window):
    # Add your code for saving the image here
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        messagebox.showinfo("Lưu", f"Lưu ảnh vào: {file_path}")