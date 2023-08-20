import tkinter as tk
from client import *
from kill import * 
from start import *
from tkinter import ttk

def kill_process(window): #code o day
    open_kill(window)

def xem_process(window):
    pass

def start_process(window):
    open_start(window)

def xoa_process(window):
    pass


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

    window.listView1 = ttk.Treeview(window, columns=("ID Process", "Count Thread"))
    window.listView1.heading("#0", text="Name Process")
    window.listView1.heading("ID Process", text="ID Process")
    window.listView1.heading("Count Thread", text="Count Thread")
    window.listView1.column("#0", width=100)  # Adjust the width of the columns
    window.listView1.column("ID Process", width=80)
    window.listView1.column("Count Thread", width=100)
    window.listView1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Configure grid weights to make the Treeview expand
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    window.mainloop()
