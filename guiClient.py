import socket
import tkinter as tk
from tkinter import messagebox

class TCPClient:
    def __init__(self, master):
        self.master = master
        self.master.title('TCP Client')

        # GUI Components
        self.label = tk.Label(master, text="Enter your message:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self):
        msg = self.entry.get()
        if not msg:
            messagebox.showinfo("Info", "Please enter a message to send.")
            return
        
        try:
            # Connect to the server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('0.0.0.0', 4444))
            client_socket.sendall(msg.encode())
            client_socket.close()
            messagebox.showinfo("Info", "Message sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send the message. Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TCPClient(root)
    root.mainloop()

