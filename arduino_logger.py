import tkinter as tk
from tkinter import filedialog
import serial
import threading

class ArduinoLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Arduino Data Logger")
        self.root.geometry("400x200")
        
        self.serial_port = None
        self.logging = False
        
        self.port_label = tk.Label(root, text="Serial Port:")
        self.port_label.pack(pady=5)
        
        self.port_entry = tk.Entry(root)
        self.port_entry.pack(pady=5)
        
        self.baud_label = tk.Label(root, text="Baud Rate:")
        self.baud_label.pack(pady=5)
        
        self.baud_entry = tk.Entry(root)
        self.baud_entry.insert(0, "9600")
        self.baud_entry.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.status_label = tk.Label(root, text="Status: Not logging")
        self.status_label.pack(pady=5)
    
    def start_logging(self):
        port = self.port_entry.get()
        baud = self.baud_entry.get()
        
        try:
            self.serial_port = serial.Serial(port, int(baud))
            self.logging = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Logging")
            
            self.log_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not self.log_file:
                self.stop_logging()
                return
            
            self.thread = threading.Thread(target=self.log_data)
            self.thread.start()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")
    
    def stop_logging(self):
        if self.serial_port:
            self.logging = False
            self.serial_port.close()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="Status: Not logging")
    
    def log_data(self):
        with open(self.log_file, 'w') as file:
            while self.logging:
                try:
                    if self.serial_port.in_waiting > 0:
                        line = self.serial_port.readline().decode('utf-8').strip()
                        file.write(line + '\n')
                        self.status_label.config(text=f"Status: Logging - {line}")
                except Exception as e:
                    self.status_label.config(text=f"Error: {e}")
                    break
        self.stop_logging()

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoLogger(root)
    root.mainloop()
