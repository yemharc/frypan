from tkinter import *

import Frypan_Controllers.window_control as window_control
import Frypan_Controllers.menu_control as menu_control

root = Tk()
root.title("프라이팬")
window_control.CenterScreen(root, 1024, 768)
root.config(menu=menu_control.BasicWindowMenu(root))

root.mainloop()