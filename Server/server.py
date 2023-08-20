from tkinter import *
import threading
import socket

class Server(Tk):
    def __init__(self):
        super().__init__()
        self.components = None
        self.server_socket = None
        self.is_running = False

    def initialize_component(self):
        self.title("Server")
        self.geometry("124x88")
        self.button1 = Button(self)
        self.button1.place(x=21, y=12, width=75, height=64)
        self.button1.config(text="Mở server", command=self.button1_Click)

    def button1_Click(self):
        if not self.is_running:
            # Start the server in a separate thread
            server_thread = threading.Thread(target=self.start_server)
            server_thread.start()

    def start_server(self):
        host = ''  # Empty string represents your computer's default IP address
        port = 12345  # Choose a suitable port number

        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Bind the socket to a specific host and port
            self.server_socket.bind((host, port))

            # Listen for incoming connections
            self.server_socket.listen(1)

            self.is_running = True
            print("Server is listening for connections...")

            while self.is_running:
                # Accept a client connection
                client_socket, address = self.server_socket.accept()
                print(f"Connected with client: {address}")

                # Add your server logic here to handle client requests

        except socket.error as e:
            print(f"Error occurred: {str(e)}")

        finally:
            # Close the server socket
            if self.server_socket is not None:
                self.server_socket.close()

    def destroy(self):
        self.dispose()
        super().destroy()

    def dispose(self):
        if self.components is not None:
            self.components.Dispose()
        self.stop_server()

    def stop_server(self):
        self.is_running = False

    def run(self):
        self.initialize_component()
        self.mainloop()


if __name__ == "__main__":
    form = Server()
    form.run()
