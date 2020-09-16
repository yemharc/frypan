from tkinter import *
import pandas as pd

import Frypan_Controllers.window_control as window_control
import Frypan_Controllers.menu_control as menu_control
import Frypan_Controllers.msgbox_control as msgbox_control
import Frypan_Controllers.data_control as data_control

root = Tk()
root.title("프라이팬")

window_control.CenterScreen(root, 1024, 768)
root.config(menu=menu_control.BasicWindowMenu(root))

frame_left = LabelFrame(root, text="GRID", relief="solid")
frame_left.pack(side="left", fill="both", expand=True)

df = data_control.get_data()

print(df)
# popup = msgbox_control.PopUp()

# Button(root, command=lambda : popup.yes_no_cancel("test111", "test222"), text="test").pack()
# Button(root, command=popup.get_res, text="Get Res").pack()

root.mainloop()