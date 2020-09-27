import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdig

import os
import threading
import pandas as pd

from Frypan_Controllers import window_control
from Frypan_Controllers import data_control
from Frypan_Controllers import msgbox_control
from Frypan_Controllers import progress_control
from Frypan_Window import preview_window

class MergeWindow:
    def __init__(self, window, notebook):
        self.root = window
        self.padding = 2
        self.padx = self.pady = self.ipadx = self.ipady = self.padding
        
        self.df_merge = pd.DataFrame()
        self.df_header = []
        
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
        
        self._btn_merge_file = tk.Button(_fm_btn, width=20, text="파일 합치기", command=lambda:threading.Thread(target=self.start_merge).start())
        self._btn_merge_file.config(state=tk.DISABLED)
        self._btn_merge_file.pack(side="right")
        
        self._pgbar = progress_control.Progress(_fm_btn, "right", "x")
        self._pgbar.clear()
        
        # File listbox & scrollbar
        _lfm_list = tk.LabelFrame(self.frm_merge, text="파일목록", padx=self.padx, pady=self.pady)
        _lfm_list.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        _sc_list_scrollbar = tk.Scrollbar(_lfm_list)
        _sc_list_scrollbar.pack(side="right", fill="y")
        # _sc_list_scrollbar.pack()

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
        
        _btn_dest_path = tk.Button(_lfm_dest_path, text="찾아보기", width=10, command=self.dest_files)
        _btn_dest_path.pack(side="right")
        
        # Options
        _lfm_opts = tk.LabelFrame(self.frm_merge, text="옵션", padx=self.padx, pady=self.pady)
        _lfm_opts.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        
        # Options - save file name
        _l_opts_filename = tk.Label(_lfm_opts, text="파일명")
        _l_opts_filename.grid(column=0, row=0, padx=self.padx, pady=self.pady)
        self._entry_opts_filename = tk.Entry(_lfm_opts, width=10, justify="center")
        self._entry_opts_filename.insert(0, "out")
        self._entry_opts_filename.grid(column=0, row=1, padx=self.padx, pady=self.pady)
        
        # Options - select DataFrame header
        _l_opts_df_header = tk.Label(_lfm_opts, text="컬럼 선택")
        _l_opts_df_header.grid(column=1, row=0, padx=self.padx, pady=self.pady)
        _btn_opts_df_header = ttk.Button(_lfm_opts, text="선택하기", width=10, command=self.select_header)
        _btn_opts_df_header.grid(column=1, row=1, padx=self.padx, pady=self.pady)
        
        # Save & Next
        _fm_save_next = tk.Frame(self.frm_merge, padx=self.padx, pady=self.pady)
        _fm_save_next.pack(fill="x", ipadx=self.ipadx, ipady=self.ipady)
        self._btn_save_next = tk.Button(_fm_save_next, text="저장하기", width=20, command=self.save_files)
        self._btn_save_next.pack(side="right")
        
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
        self.df_merge = pd.DataFrame(data=None)
        
        if self._lb_listbox.size() == 0:
            self._btn_merge_file.config(state=tk.DISABLED)

    def dest_files(self):
        dm = data_control.DataMgr()
        _dest_dir = dm.GetDir()
        
        if _dest_dir == "":
            return
        
        self._entry_dest_path.config(state="normal")
        self._entry_dest_path.delete(0, tk.END)
        self._entry_dest_path.insert(0, _dest_dir)
        self._entry_dest_path.config(state="readonly")

    def save_files(self):
        pop = msgbox_control.PopUp()
        
        if self.df_merge.size == 0:
            pop.warning("파일 저장", "저장할 데이터가 없습니다")
        elif len(str(self._entry_dest_path.get())) == 0:
            pop.warning("파일 저장", "저장할 경로를 선택하세요")
        else:
            dest = str(self._entry_dest_path.get()) + "/" + self._entry_opts_filename.get() + ".csv"
            if os.path.isfile(dest):
                pop.yes_no("파일 저장", "파일을 덮어쓸까요?")
                if pop.get_res():
                    self.df_merge.to_csv(dest, sep=",", encoding="utf-8-sig")
                    pop.info("파일 저장", "파일을 덮어썼습니다")
                else:
                    pop.warning("파일 저장", "파일명을 변경하세요")
                    self._entry_opts_filename.focus_set()
            else:
                self.df_merge.to_csv(dest, sep=",", encoding="utf-8-sig")
                pop.info("파일 저장", "파일을 저장했습니다")
                
    def select_header(self):
        header = list(self.df_merge.columns)
        preview = preview_window.Preview(self.root, "merge_opts", "헤더 선택", 640, 480)
        preview.df_select_header(header)

    def start_merge(self):
        self._pgbar.start()
        dm = data_control.DataMgr()
        pop = msgbox_control.PopUp()
        list_to_files = self._lb_listbox.get(0, tk.END)
        try:
            self.df_merge = dm.Merge(self.df_merge, list_to_files)
            print(self.df_merge)
            self._pgbar.complete()
            pop.info("파일 합치기", "작업완료")
        except:
            pop.error("파일 합치기", "실패!")
            
        if pop.get_res():
            self._pgbar.clear()
            
    def preview(self):
        preview = preview_window.Preview(self.root, "merge_opts", "미리보기", 640, 480)
        preview.df_preview(self.df_merge)
        print(self.df_header)