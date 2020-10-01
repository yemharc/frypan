import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

from Frypan_Controllers import window_control

from Frypan_Window import menu_window
from Frypan_Window import merge_window

class FrypanMain:
    def __init__(self, master):
        self.root = master
        self.root.title("프라이팬")
        
        self.root.config(menu=menu_window.BasicWindowMenu(self.root))
        window_control.CenterScreen(self.root, 800, 600)
        
        notebook = ttk.Notebook(
            self.root,
            width=window_control.GetScreenSize(self.root, "ws"),
            height=window_control.GetScreenSize(self.root, "hs"),
            takefocus=True)
        notebook.enable_traversal()
        notebook.pack()
        
        merge_window.MergeWindow(self.root, notebook)
        
        frame2 = tk.Frame(root)
        notebook.add(frame2, text="데이터 매칭")
        label2 = tk.Label(frame2, text="개발중")
        label2.pack()

        frame3 = tk.Frame(root)
        notebook.add(frame3, text="데이터 분석")
        label3 = tk.Label(frame3, text="개발중")
        label3.pack()
        
root = tk.Tk()
startapp = FrypanMain(root)
root.mainloop()