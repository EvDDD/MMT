import tkinter as tk
from client import *
from process import *
from connect_server import *

def butNhap_Click(new_window):
    # Add your code here for the button click event
    message = "kill"
    globals.client_socket.send(message.encode())

    nameProApp = new_window.txtID.get()
    globals.client_socket.send(nameProApp.encode())

    checkOK = globals.client_socket.recv(1024).decode()
    if checkOK == "OK":
        messagebox.showinfo("", "Đã diệt ID " + nameProApp)

def open_kill(window):
    new_window = tk.Toplevel(window)
    new_window.title("Kill")

    new_window.txtID = tk.Entry(new_window)
    new_window.txtID.insert(tk.END, "Nhập ID")
    new_window.txtID.grid(row=0, column=0, padx=10, pady=10)

    new_window.butNhap = tk.Button(new_window, text="Kill", command=lambda:butNhap_Click(new_window))
    new_window.butNhap.grid(row=0, column=1, padx=10, pady=10)

