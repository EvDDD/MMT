import tkinter as tk
import json
from client import *
from kill import * 
from start import *
from tkinter import ttk
from connect_server import *

def kill_process(window): #code o day
    open_kill(window)

def xem_process(window):
    message = "pro"
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

def start_process(window):
    open_start(window)

def xoa_process(window):
    window.listView1.delete(*window.listView1.get_children())


def open_process_window(self):
    window = tk.Toplevel(self)

    window.title("Process")

    window.button1 = ttk.Button(window, text="Kill", command=lambda:kill_process(window))
    window.button1.grid(row=0, column=0, padx=10, pady=10)

    window.button2 = ttk.Button(window, text="Xem", command=lambda:xem_process(window))
    window.button2.grid(row=0, column=1, padx=10, pady=10)

    window.button3 = ttk.Button(window, text="Start", command=lambda:start_process(window))
    window.button3.grid(row=0, column=2, padx=10, pady=10)

    window.button4 = ttk.Button(window, text="Xóa", command=lambda:xoa_process(window))
    window.button4.grid(row=1, column=1, padx=10, pady=10)

    window.listView1 = ttk.Treeview(window, columns=("Name Process", "ID Process", "Count Thread"), show="headings")
    window.listView1.heading("Name Process", text="Name Process")
    window.listView1.heading("ID Process", text="ID Process")
    window.listView1.heading("Count Thread", text="Count Thread")
    window.listView1.column("Name Process", width=120)  # Adjust the width of the columns
    window.listView1.column("ID Process", width=80)
    window.listView1.column("Count Thread", width=80)
    window.listView1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Configure grid weights to make the Treeview expand
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    window.mainloop()
