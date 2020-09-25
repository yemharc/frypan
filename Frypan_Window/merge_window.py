import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdig

import pandas as pd

from Frypan_Controllers import window_control
from Frypan_Controllers import data_control
from Frypan_Controllers import msgbox_control
from Frypan_Controllers import preview_window

class MergeWindow:
    def __init__(self, window, notebook):
        self.root = window
        self.padding = 2
        self.padx = self.pady = self.ipadx = self.ipady = self.padding
        
        self.df_merge = pd.DataFrame()
        
        self.frm_merge = tk.Frame(window, padx=self.padx, pady=self.pady)
        notebook.add(self.frm_merge, text="파일 합치기")
        
        # File buttons
        _fm_btn = tk.Frame(self.frm_merge, padx=self.padx, pady=self.pady)
        _fm_btn.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        _btn_ins_file = tk.Button(_fm_btn, width=20, text="파일 추가", command=self.add_files)
        _btn_ins_file.pack(side="left")
        
        _btn_del_file = tk.Button(_fm_btn, width=20, text="파일 삭제", command=self.del_files)
        _btn_del_file.pack(side="left")
        
        self._btn_opts_preview = tk.Button(_fm_btn, text="미리보기", width=20, command=self.preview)
        self._btn_opts_preview.pack(side="left")
        
        self._btn_merge_file = tk.Button(_fm_btn, width=20, text="파일 합치기", command=self.start_merge)
        self._btn_merge_file.config(state=tk.DISABLED)
        self._btn_merge_file.pack(side="right")
        
        # File listbox & scrollbar
        _lfm_list = tk.LabelFrame(self.frm_merge, text="파일목록", padx=self.padx, pady=self.pady)
        _lfm_list.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        _sc_list_scrollbar = tk.Scrollbar(_lfm_list)
        _sc_list_scrollbar.pack(side="right", fill="y")
        _sc_list_scrollbar.pack()

        self._lb_listbox = tk.Listbox(_lfm_list,
                                        selectmod="extended",
                                        height=15,
                                        yscrollcommand=_sc_list_scrollbar.set)
        self._lb_listbox.pack(side="left", fill="both", expand=True)
        _sc_list_scrollbar.config(command=self._lb_listbox.yview)
        
        # File destination path
        _lfm_dest_path = tk.LabelFrame(self.frm_merge, text="저장경로", padx=self.padx, pady=self.pady)
        _lfm_dest_path.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        
        self._entry_dest_path = tk.Entry(_lfm_dest_path, text="폴더 선택", state="readonly")
        self._entry_dest_path.pack(side="left", fill="x", expand=True)
        
        _btn_dest_path = tk.Button(_lfm_dest_path, text="찾아보기", width=10, command=self.save_files)
        _btn_dest_path.pack(side="right")
        
        # Options
        _lfm_opts = tk.LabelFrame(self.frm_merge, text="옵션", padx=self.padx, pady=self.pady)
        _lfm_opts.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        
        _l_opts_col_cnt = tk.Label(_lfm_opts, text="헤더 행")
        _l_opts_col_cnt.grid(column=0, row=0)
        _cmb_opts_col_cnt = ttk.Combobox(_lfm_opts, state="readonly", justify="center", width=6, values=(1,2,3,4,5))
        _cmb_opts_col_cnt.grid(column=0, row=1)
        _cmb_opts_col_cnt.current(0)
        # _cmb_opts_col_cnt.bind("<<ComboboxSelected>>", self.cmb_value(_cmb_opts_col_cnt.get()))
        
        # Progress bar
        _lfm_progress = tk.LabelFrame(self.frm_merge, text="진행상황", padx=self.padx, pady=self.pady)
        _lfm_progress.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        
        _pgbar_value = tk.DoubleVar()
        _pgbar = ttk.Progressbar(_lfm_progress, maximum=100, variable=_pgbar_value)
        _pgbar.pack(fill="x")

    def add_files(self):
        dm = data_control.DataMgr()
        _files = dm.AddFiles()
        list_to_files = self._lb_listbox.get(0, tk.END)
        
        for file in _files:
            if file not in list_to_files:
                self._lb_listbox.insert(tk.END, file)
                
        if self._lb_listbox.size() > 0:
            self._btn_merge_file.config(state=tk.NORMAL)


    def del_files(self):
        for index in reversed(self._lb_listbox.curselection()):
            self._lb_listbox.delete(index)
        self._lb_listbox.selection_set(tk.END)
        
        if self._lb_listbox.size() == 0:
            self._btn_merge_file.config(state=tk.DISABLED)

    def save_files(self):
        dm = data_control.DataMgr()
        _dest_dir = dm.GetDir()
        
        if _dest_dir == "":
            return
        
        self._entry_dest_path.config(state="normal")
        self._entry_dest_path.delete(0, tk.END)
        self._entry_dest_path.insert(0, _dest_dir)
        self._entry_dest_path.config(state="readonly")

    def start_merge(self):
        dm = data_control.DataMgr()
        list_to_files = self._lb_listbox.get(0, tk.END)
        self.df_merge = dm.Merge(list_to_files)
        print(self.df_merge)
        
    def preview(self):
        return preview_window.Preview(self.root, "merge_opts", "데이터 선택", 640, 480)