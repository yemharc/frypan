import tkinter as tk

import pandas as pd

from pandastable import Table as pt

from Frypan_Controllers import window_control

from Frypan_Window import merge_window

class Preview:
    def __init__(self, root, name, title, w_width, w_height):
        self.window = tk.Toplevel(root, name=name)
        self.window.title(title)
        window_control.CenterScreen(self.window, w_width, w_height)
        self.window.focus_set()
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def df_preview(self, df):
        f = tk.Frame(self.window)
        f.pack(fill="both",expand=1)
        pt(f, dataframe=df, showtoolbar=False, showstatusbar=False).show()