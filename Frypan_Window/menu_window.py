import tkinter as tk
import tkinter.ttk as ttk

import os

from Frypan_Controllers import window_control

def BasicWindowMenu(master):
    menu = tk.Menu(master)
    menu_info = tk.Menu(menu, tearoff=0)
    menu_info.add_command(label="라이센스", command=lambda:LicenseWindow(master))
    menu_info.add_command(label="프로그램", command=lambda:ProgramInfo(master))
    menu.add_cascade(label="정보", menu=menu_info)
    
    return menu

def LicenseWindow(master):
    license_window = tk.Toplevel(master, name="LicenseWindow")
    license_window.title("라이센스")
    window_control.CenterScreen(license_window,
                                window_control.GetScreenSize(license_window, "ws")//3,
                                window_control.GetScreenSize(license_window, "hs")//3)
    license_window.resizable(False, False)
    
    _fm_license = tk.Frame(license_window)
    _fm_license.pack(fill=tk.BOTH, expand=True)
    
    _txtfile = open(os.path.abspath(".") + "/LICENSE", "r")
    _txt = _txtfile.read()
    _txtfile.close()
    
    _txt_license = tk.Text(_fm_license)
    _txt_license.insert(1.0, _txt)
    _txt_license.config(state=tk.DISABLED)
    _txt_license.pack(fill=tk.BOTH, expand=True)
    
    
def ProgramInfo(window):
    proginfo_window = tk.Toplevel(window, name="ProgramInfo")
    proginfo_window.title("프로그램 정보")
    window_control.CenterScreen(proginfo_window,
                                window_control.GetScreenSize(proginfo_window, "ws")//3,
                                window_control.GetScreenSize(proginfo_window, "hs")//3)
    proginfo_window.resizable(False, False)
    
    _fm_proginfo = tk.Frame(proginfo_window)
    _fm_proginfo.pack(fill=tk.BOTH, expand=True)
    
    _txtfile = open(os.path.abspath(".") + "/INFO", "r")
    _txt = _txtfile.read()
    _txtfile.close()
    
    _txt_proginfo = tk.Text(_fm_proginfo)
    _txt_proginfo.insert(1.0, _txt)
    _txt_proginfo.config(state=tk.DISABLED)
    _txt_proginfo.pack(fill=tk.BOTH, expand=True)