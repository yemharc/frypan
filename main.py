import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import pandas as pd

import Frypan_Controllers.window_control as window_control
import Frypan_Controllers.menu_control as menu_control
import Frypan_Controllers.msgbox_control as msgbox_control
import Frypan_Controllers.data_control as data_control

import Frypan_Window.merge_window as merge_window

# MAIN WINDOW START
window = tk.Tk()
window.title("프라이팬")
window_control.CenterScreen(window, 800, 600)
window.minsize(800, 600)

def_font = tkfont.nametofont(("TkDefaultFont"))
def_font.config(size=9)

window_style = ttk.Style(window)
window_style.theme_use("default")
window_style.configure("Tab", focuscolor=window_style.configure(".")["background"])

# window.config(menu=menu_control.BasicWindowMenu(window))
# MAIN WINDOW END

# TAB WINDOW START
notebook = ttk.Notebook(
    window,
    width=window_control.GetScreenSize(window, "ws"),
    height=window_control.GetScreenSize(window, "hs"),
    takefocus=True)
notebook.enable_traversal()
notebook.pack()
# TAB WINDOW END

w_merge = merge_window.MergeWindow(window, notebook)

frame2 = tk.Frame(window)
notebook.add(frame2, text="데이터 매칭")
label2 = tk.Label(frame2, text="개발중")
label2.pack()

frame3 = tk.Frame(window)
notebook.add(frame3, text="데이터 분석")
label3 = tk.Label(frame3, text="개발중")
label3.pack()

# df = data_control.get_data()
# print(df)
# popup = msgbox_control.PopUp()

# Button(window, command=lambda : popup.yes_no_cancel("test111", "test222"), text="test").pack()
# Button(window, command=popup.get_res, text="Get Res").pack()

# Start window
window.mainloop()