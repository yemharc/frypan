import tkinter as tk

import pandas as pd

from pandastable import Table as pt

from Frypan_Controllers import window_control

from Frypan_Window import merge_window

class Preview:
    def __init__(self, root, name, title, w_width, w_height):
        self.window = tk.Toplevel(root, name=name)
        self.window.title(title)
        window_control.CenterScreen(self.window, w_width, w_height)
        self.window.grab_set()
        self.window.focus_set()
        
        self._pv_df_header = []
        self.return_df_header = []
        self._chk_df_header = []
        self._chk_var = dict()
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def quit(self):
        self.window.destroy()
        
    def df_select_header(self, header):
        self._pv_df_header = header
        _lfm_df_select = tk.LabelFrame(self.window, text="데이터를 선택하세요")
        _lfm_df_select.pack(fill=tk.BOTH, ipadx=4, ipady=4)
        
        _btn_df_select = tk.Button(_lfm_df_select, text="전체선택", command=lambda:self.df_select_header_all(1))
        _btn_df_select.pack(side=tk.LEFT)
        _btn_df_select = tk.Button(_lfm_df_select, text="전체해제", command=lambda:self.df_select_header_all(0))
        _btn_df_select.pack(side=tk.LEFT)
        _btn_df_select = tk.Button(_lfm_df_select, text="선택완료", command=self.quit)
        _btn_df_select.pack(side=tk.LEFT)
        
        _df_select_cv = tk.Canvas(self.window)
        sc = tk.Scrollbar(self.window, orient=tk.VERTICAL, command=_df_select_cv.yview)
        _f_header = tk.Frame(_df_select_cv)
        
        count = 0
        rows = 0
        
        for child in self._pv_df_header:
            for c in range(3):
                if count < len(self._pv_df_header):
                    self._chk_var[count] = tk.IntVar()
                    _chks = tk.Checkbutton(_f_header, text=self._pv_df_header[count], variable=self._chk_var[count],
                                                    command=lambda count=count:self.df_select_cb(count, self._pv_df_header), onvalue=1, offvalue=0)
                    _chks.grid(column=c, row=rows, sticky="w")
                    self._chk_df_header.append(_chks)
                    count += 1
            rows += 1
        
        _df_select_cv.create_window(0, 0, anchor='nw', window=_f_header)
        _df_select_cv.update_idletasks()
        _df_select_cv.configure(scrollregion=_df_select_cv.bbox('all'), yscrollcommand=sc.set)
        
        sc.pack(side="right", fill="y")
        _df_select_cv.pack(fill='both', expand=True, side='left')
        
    def df_select_header_all(self, select):
        self.return_df_header = []
        tag = 0
        
        for i in self._chk_df_header:
            if select:
                i.select()
            else:
                i.deselect()
                
        for i in self._chk_df_header:
            if self._chk_var[tag].get():
                self.return_df_header.append(self._pv_df_header[tag])
            tag += 1
        
    def df_select_cb(self, i, header):
        self.return_df_header = []
        tag = 0
        for i in self._chk_df_header:
            if self._chk_var[tag].get():
                self.return_df_header.append(self._pv_df_header[tag])
            tag += 1
            
        print(self.return_df_header)
            
    def df_preview(self, df):
        f = tk.Frame(self.window)
        f.pack(fill="both",expand=1)
        pt(f, dataframe=df, showtoolbar=False, showstatusbar=False).show()