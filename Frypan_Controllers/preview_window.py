import tkinter as tk

from Frypan_Controllers import window_control

class Preview:
    def __init__(self, window, name, title, w_width, w_height):
        window = tk.Toplevel(window, name=name)
        window.title(title)
        window_control.CenterScreen(window, w_width, w_height)
        window.grab_set()
        window.focus_set()
    
    def __del__(self):
        print("delete instance : ", __name__)