import tkinter as tk
import tkinter.ttk as ttk

class Progress:
    def __init__(self):
        pass
    
    def __del__(self):
        print("delete instance : ", __name__)
        
    def make(self, frame, max):
        # _pgbar_value = tk.DoubleVar()
        return ttk.Progressbar(frame, maximum=max, variable=tk.DoubleVar())

# p_var = DoubleVar()
# pgbar = ttk.Progressbar(root, maximum=100, length=200, variable=p_var)
# pgbar.pack()

# def btncmd1():
#     pgbar.config(mode="determinate")
#     pgbar.stop()
    
# def btncmd2():
#     for i in range(1, 101):
#         time.sleep(0.01)
#         p_var.set(i)
#         pgbar.update()

# btn1 = Button(root, text="start", command=btncmd1)
# btn1.pack()

# btn2 = Button(root, text="stop", command=btncmd2)
# btn2.pack()
