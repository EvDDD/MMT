import tkinter as tk
import socket
from process import *
from pic import *
from listApp import *
from keylog import *
from connect_server import *

def getIP(self):
    ip = self.txtIP.get()
    return ip

class ClientForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.components = None

        self.initialize_components()

    def initialize_components(self):
        self.geometry("372x302")
        self.title("Client")

        self.txtIP = tk.Entry(self)
        self.txtIP.insert(0, "Nhập IP")
        self.txtIP.place(x = 12, y = 29, width=226, height=20)

        self.butConnect = tk.Button(self, text="Kết nối", command=self.butConnect_click)
        self.butConnect.place(x = 244, y = 27, width=100, height=23)

        self.butApp = tk.Button(self, text="App Running", command=self.butApp_click)
        self.butApp.place(x = 93, y = 64, width=145, height=63)

        self.butTat = tk.Button(self, text="Tắt máy", command=self.butTat_click)
        self.butTat.place(x = 147, y = 133, width=91, height=57)

        self.butReg = tk.Button(self, text="Chụp màn hình", command=self.butPic_click)
        self.butReg.place(x=93, y=196, width=251, height=65)

        self.butPic = tk.Button(self, text="Thoát", command=self.butExit_click)
        self.butPic.place(x=93, y=133, width=48, height=57)

        self.butKeyLock = tk.Button(self, text="Keystroke", command=self.butKeyLock_click)
        self.butKeyLock.place(x = 244, y = 64, width=100, height=126)

        self.butProcess = tk.Button(self, text="Process Running",wraplength=70, command=self.butProcess_click)
        self.butProcess.place(x = 12, y = 64, width=75, height=197)

    def butApp_click(self):
        # Event handler for the "App Running" button
        open_app_window(self)

    def butConnect_click(self):
        ip = getIP(self)
        connect_to_server(ip)
        if globals.client_socket is None:
            print("F")

    def butTat_click(self):
        # Event handler for the "Tắt máy" button
        pass

    def butExit_click(self):    
        # Event handler for the "Thoát" button
        # cái nút này vậy là xong rồi, nó chỉ là nút tắt chương trình
        globals.client_socket.close()
        self.destroy()

    def butPic_click(self):
        # Event handler for the "Chụp màn hình" button
        open_pic_window(self)
        

    def butKeyLock_click(self):
        # Event handler for the "Keystroke" button
        open_keylog_window(self)

    def butProcess_click(self):
        # Event handler for the "Process Running" button
        open_process_window(self)

if __name__ == "__main__":
    client_form = ClientForm()
    client_form.mainloop()
