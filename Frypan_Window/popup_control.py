import tkinter.messagebox as popup
import tkinter.filedialog as fd

class PopUp:
    def __init__(self):
        self.res = None
        self.title = None
        self.text = None
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def get_res(self):
        return self.res

    def info(self, title, text):
        popup.showinfo(title, text)
        self.res = 1
        
    def warning(self, title, text):
        self.res = popup.showwarning(title, text)

    def error(self, title, text):
        popup.showerror(title, text)
        self.res = 1

    def yes_no(self, title, text):
        self.res = popup.askyesno(title, text)

    def yes_no_cancel(self, title, text):
        self.res = popup.askyesnocancel(title, text)

    def selection(self, title, text):
        self.res = popup.askokcancel(title, text)

    def retry(self, title, text):
        self.res = popup.askretrycancel(title, text)

    # def open_file(self):
    #     file = fd.askopenfilename()
    #     txt = file.read()
    #     print(type(txt))
    #     file.close()