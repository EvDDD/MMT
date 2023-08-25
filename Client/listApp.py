import tkinter as tk
import json
from client import *
from kill import * 
from start import *
from tkinter import ttk
from connect_server import *

def kill_app(window):
    open_kill(window)

def xem_app(window):
    message = "app"
    globals.client_socket.send(message.encode())

    # Receive the string representation of processes from the server
    buffer = b""
    
    data = globals.client_socket.recv(8388608)  # Receive data in chunks of 8MB
    
    buffer += data  # Append the received data to the buffer

    # Decode the received data
    received_data = buffer.decode()

    # Parse the JSON string into a list of processes
    process_list = json.loads(received_data)

    for process in process_list:
        pid = process['pid']
        name = process['name']
        num_threads = process['num_threads']
        
        window.listView1.insert('', tk.END, values=(name, pid, num_threads))

def start_app(window):
    open_start(window)

def xoa_app(window):
    window.listView1.delete(*window.listView1.get_children())

def open_app_window(self):
    window = tk.Toplevel(self)

    window.title("listApp")

    window.button1 = ttk.Button(window, text="Kill", command=lambda:kill_app(window))
    window.button1.grid(row=0, column=0, padx=10, pady=10)

    window.button2 = ttk.Button(window, text="Xem", command=lambda:xem_app(window))
    window.button2.grid(row=0, column=1, padx=10, pady=10)

    window.button3 = ttk.Button(window, text="Start", command=lambda:start_app(window))
    window.button3.grid(row=0, column=2, padx=10, pady=10)

    window.button4 = ttk.Button(window, text="Xóa", command=lambda:xoa_app(window))
    window.button4.grid(row=1, column=1, padx=10, pady=10)

    window.listView1 = ttk.Treeview(window, columns=("Name Application", "ID Application", "Count Thread"), show="headings")
    window.listView1.heading("Name Application", text="Name Application")
    window.listView1.heading("ID Application", text="ID Application")
    window.listView1.heading("Count Thread", text="Count Thread")
    window.listView1.column("Name Application", width=120)  # Adjust the width of the columns
    window.listView1.column("ID Application", width=80)
    window.listView1.column("Count Thread", width=80)
    window.listView1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Configure grid weights to make the Treeview expand
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    window.mainloop()
