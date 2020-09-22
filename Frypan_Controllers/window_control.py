def CenterScreen(win, w_width, w_height):
    s_width = (GetScreenSize(win, "ws") // 2) - (w_width // 2)
    s_height = (GetScreenSize(win, "hs") // 2) - (w_height // 2)
    win.geometry('{}x{}+{}+{}'.format(w_width, w_height, s_width, s_height))
    
def GetScreenSize(window, axis):
    if axis == 'ws':
        return window.winfo_screenwidth()
    elif axis == 'hs':
        return window.winfo_screenheight()
    elif axis == 'w':
        return window.winfo_reqwidth()
    elif axis == 'h':
        return window.winfo_reqheight()

def SetPadding(frame, x, y):
        for child in frame.winfo_children():
            child.config(padx=x, pady=y)