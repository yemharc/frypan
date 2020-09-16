import tkinter.messagebox as msgbox
import tkinter.filedialog as fd

class PopUp:
    def __init__(self):
        self.res = None
        self.title = None
        self.text = None
        
    def __del__(self):
        print("delete instance")
        
    def get_res(self):
        return print(self.res)

    def info(self, title, text):
        self.res = msgbox.showinfo(title, text)
        
    def warning(self, title, text):
        self.res = msgbox.showwarning(title, text)

    def error(self, title, text):
        self.res = msgbox.showerror(title, text)

    def yes_no(self, title, text):
        self.res = msgbox.askyesno(title, text)

    def yes_no_cancel(self, title, text):
        self.res = msgbox.askyesnocancel(title, text)

    def selection(self, title, text):
        self.res = msgbox.askokcancel(title, text)

    def retry(self, title, text):
        self.res = msgbox.askretrycancel(title, text)

    def open_file(self):
        file = fd.askopenfilename()
        txt = file.read()
        print(type(txt))
        file.close()