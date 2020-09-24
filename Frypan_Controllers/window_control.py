import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import tkinter.filedialog as fdig

def CenterScreen(window, w_width, w_height):
    s_width = (GetScreenSize(window, "ws") // 2) - (w_width // 2)
    s_height = (GetScreenSize(window, "hs") // 2) - (w_height // 2)
    window.geometry('{}x{}+{}+{}'.format(w_width, w_height, s_width, s_height))
    
    window.minsize(w_width, w_height)
    def_font = tkfont.nametofont(("TkDefaultFont"))
    def_font.config(size=9)
    
    window_style = ttk.Style(window)
    # window_style.theme_use("default")
    window_style.configure("Tab", focuscolor=window_style.configure(".")["background"])
    
def GetScreenSize(window, axis):
    if axis == 'ws':
        return window.winfo_screenwidth()
    elif axis == 'hs':
        return window.winfo_screenheight()
    elif axis == 'w':
        return window.winfo_reqwidth()
    elif axis == 'h':
        return window.winfo_reqheight()