# screen_name, width, height
def CenterScreen(win, w_width, w_height):
    s_width = (win.winfo_screenwidth() // 2) - (w_width // 2)
    s_height = (win.winfo_screenheight() // 2) - (w_height // 2)
    win.geometry('{}x{}+{}+{}'.format(w_width, w_height, s_width, s_height))