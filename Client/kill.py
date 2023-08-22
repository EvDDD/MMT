import tkinter as tk
from client import *
from process import *
from connect_server import *

def butNhap_Click(new_window):
    # Add your code here for the button click event
    pass

def open_kill(window):
    new_window = tk.Toplevel(window)
    new_window.title("Kill")

    new_window.butNhap = tk.Button(new_window, text="Kill", command=butNhap_Click(new_window))
    new_window.butNhap.grid(row=0, column=1, padx=10, pady=10)

    new_window.txtID = tk.Entry(new_window)
    new_window.txtID.insert(tk.END, "Nhập ID")
    new_window.txtID.grid(row=0, column=0, padx=10, pady=10)
    