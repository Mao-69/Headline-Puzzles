import tkinter as tk
from tkinter import filedialog, messagebox
import json

class LargeGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("50x50 Letter Grid")
        self.grid_entries = {}
        self.canvas = tk.Canvas(root)
        self.scroll_frame = tk.Frame(self.canvas)
        self.scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_y = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.scrollbar_y.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.create_grid()

    def create_grid(self):
        for row in range(30):
            for col in range(50):
                entry = tk.Entry(self.scroll_frame, width=2, font=("Arial", 10))
                entry.grid(row=row, column=col)
                self.grid_entries[(row, col)] = entry

root = tk.Tk()
app = LargeGridApp(root)
root.mainloop()
