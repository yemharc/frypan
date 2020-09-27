import tkinter as tk

import pandas as pd

from pandastable import Table as pt
from Frypan_Controllers import window_control

class Preview:
    def __init__(self, window, name, title, w_width, w_height, df):
        window = tk.Toplevel(window, name=name)
        window.title(title)
        window_control.CenterScreen(window, w_width, w_height)
        window.grab_set()
        window.focus_set()

        f = tk.Frame(window)
        f.pack(fill="both",expand=1)
        pt(f, dataframe=df, showtoolbar=False, showstatusbar=False).show()
        
    def __del__(self):
        print("delete instance : ", __name__)