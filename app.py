import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Precision analysis")
        root.geometry('800x600')
        
        self.file1_path = None
        self.file2_path = None
        
        self.create_widgets()
    
    def create_widgets(self):
        return

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()