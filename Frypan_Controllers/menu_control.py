from tkinter import *

def BasicWindowMenu(win):
    menu = Menu(win)
    
    # File
    menu_file = Menu(menu, tearoff=0)
    menu_file.add_command(label="파일")
    menu_file.add_command(label="123")
    menu_file.add_separator()
    menu_file.add_command(label="Save All", state="disable")
    menu_file.add_separator()
    menu_file.add_command(label="Exit", command=win.quit)
    menu.add_cascade(label="File", menu=menu_file)
    
    # Edit
    menu_edit = Menu(menu, tearoff=0)
    menu_edit.add_radiobutton(label="test1")
    menu_edit.add_radiobutton(label="test2")
    menu_edit.add_radiobutton(label="test3")
    menu.add_cascade(label="Edit", menu=menu_edit)
    
    # View
    menu_view = Menu(menu, tearoff=0)
    menu_view.add_checkbutton(label="Show1")
    menu_view.add_checkbutton(label="Show2")
    menu_view.add_checkbutton(label="Show3")
    menu.add_cascade(label="View", menu=menu_view)
    
    return (menu)