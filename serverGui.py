import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext

class TCPServer:
    def __init__(self, master):
        self.master = master
        self.master.title('TCP Server')

        self.label_port = tk.Label(master, text="Enter desired port:")
        self.label_port.pack(pady=10)

        self.entry_port = tk.Entry(master, width=50)
        self.entry_port.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Server", command=self.start_server)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.label_info = tk.Label(master, text="Server not started.")
        self.label_info.pack(pady=10)

        self.text_box = scrolledtext.ScrolledText(master, width=50, height=10)
        self.text_box.pack(pady=10)

        self.server_socket = None
        self.server_thread = None
        self.is_running = threading.Event()  # Event to handle server loop termination

    def start_server(self):
        port = self.entry_port.get()
        if not port.isdigit():
            messagebox.showerror("Error", "Please enter a valid port number.")
            return

        port = int(port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.settimeout(1)  # Set a timeout of 1 second
        try:
            self.server_socket.bind(('192.168.0.110', port))
            self.server_socket.listen(5)
            self.label_info.config(text=f"Server started on 0.0.0.0:{port}")
            self.is_running.set()
            self.server_thread = threading.Thread(target=self.listen_for_clients)
            self.server_thread.start()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to start the server. Error: {e}")

    def listen_for_clients(self):
        while self.is_running.is_set():
            try:
                client_socket, client_address = self.server_socket.accept()
                threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()
            except socket.timeout:  # This exception is raised when accept() times out
                continue
            except Exception as e:
                self.text_box.insert(tk.END, f"Server error: {e}\n")

    def handle_client(self, client_socket, client_address):
        data = client_socket.recv(1024)
        message = data.decode()
        self.text_box.insert(tk.END, f"Received from {client_address}: {message}\n")
        client_socket.close()

    def stop_server(self):
        self.is_running.clear()
        if self.server_socket:
            self.server_socket.close()  # This will raise an exception in the listening thread, which we catch.
        self.label_info.config(text="Server stopped.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TCPServer(root)
    try:
        root.iconbitmap("monitor.ico")
    except Exception as e:
        print(f"Failed to set the icon due to {e}")
    root.mainloop()

