import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import pandas as pd

import Frypan_Controllers.window_control as window_control
import Frypan_Controllers.menu_control as menu_control
import Frypan_Controllers.msgbox_control as msgbox_control
import Frypan_Controllers.data_control as data_control

import Frypan_Window.merge_window as merge_window

# # MAIN WINDOW START
root = tk.Tk()
root.title("프라이팬")
window_control.CenterScreen(root, 800, 600)
# window.config(menu=menu_control.BasicWindowMenu(window))
# # MAIN WINDOW END

# # TAB WINDOW START
notebook = ttk.Notebook(
    root,
    width=window_control.GetScreenSize(root, "ws"),
    height=window_control.GetScreenSize(root, "hs"),
    takefocus=True)
notebook.enable_traversal()
notebook.pack()
# # TAB WINDOW END

w_merge = merge_window.MergeWindow(root, notebook)

frame2 = tk.Frame(root)
notebook.add(frame2, text="데이터 매칭")
label2 = tk.Label(frame2, text="개발중")
label2.pack()

frame3 = tk.Frame(root)
notebook.add(frame3, text="데이터 분석")
label3 = tk.Label(frame3, text="개발중")
label3.pack()

# # df = data_control.get_data()
# # print(df)
# # popup = msgbox_control.PopUp()

# # Button(window, command=lambda : popup.yes_no_cancel("test111", "test222"), text="test").pack()
# # Button(window, command=popup.get_res, text="Get Res").pack()

# Start window
if __name__ == "__main__":
    root.mainloop()