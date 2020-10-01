import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdig

import os
import threading
import pandas as pd

from Frypan_Controllers import window_control
from Frypan_Controllers import data_control
from Frypan_Controllers import progress_control

from Frypan_Window import popup_control
from Frypan_Window import preview_window

class MergeWindow:
    def __init__(self, master, notebook):
        self.root = master
        self.nb = notebook
        self.padx = self.pady = self.ipadx = self.ipady = self.padding = 2
        
        self.frm_merge = tk.Frame(None, padx=self.padx, pady=self.pady)
        self.nb.add(self.frm_merge, text="파일 합치기")
        
        self.df_merge = pd.DataFrame(data=None)
        
        self.file_control()
        self.file_listbox()
        self.file_dest()
        self.file_opt()
        
        
        
    # Views
    def file_control(self):
        file_control_fm = tk.Frame(self.frm_merge, padx=self.padx, pady=self.pady)
        file_control_fm.pack(fill=tk.X, ipadx=self.ipadx, ipady=self.ipady)
        self.file_control_btn_ins_file = tk.Button(file_control_fm, width=20, text="파일 추가", command=self.add_files)
        self.file_control_btn_ins_file.pack(side=tk.LEFT)
        
        self.file_control_btn_del_file = tk.Button(file_control_fm, width=20, text="파일 삭제", command=self.del_files)
        self.file_control_btn_del_file.pack(side=tk.LEFT)
        
        self.file_control_btn_opts_preview = tk.Button(file_control_fm, text="미리보기", width=20, command=self.preview_files)
        self.file_control_btn_opts_preview.pack(side=tk.LEFT)
        
        self.file_control_btn_merge_file = tk.Button(file_control_fm, width=20, text="파일 합치기", command=lambda:threading.Thread(target=self.merge_files).start())
        self.file_control_btn_merge_file.config(state=tk.DISABLED)
        self.file_control_btn_merge_file.pack(side=tk.RIGHT)
        
        self.file_control_pgbar = progress_control.Progress(file_control_fm, tk.RIGHT, tk.X)
        self.file_control_pgbar.clear()
        
    def file_listbox(self):
        file_listbox_lfm = tk.LabelFrame(self.frm_merge, text="파일목록", padx=self.padx, pady=self.pady)
        file_listbox_lfm.pack(fill=tk.X, ipadx=self.ipadx, ipady=self.ipady)
        self.file_listbox_sc_list = tk.Scrollbar(file_listbox_lfm)
        self.file_listbox_sc_list.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.file_listbox_lb = tk.Listbox(
            file_listbox_lfm,
            selectmod=tk.EXTENDED,
            height=15,
            yscrollcommand=self.file_listbox_sc_list.set)
        self.file_listbox_lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_listbox_sc_list.config(command=self.file_listbox_lb.yview)
        
    def file_dest(self):
        self.file_dest_lfm = tk.LabelFrame(
            self.frm_merge,
            text="저장경로",
            padx=self.padx,
            pady=self.pady)
        self.file_dest_lfm.pack(fill=tk.X, ipadx=self.ipadx, ipady=self.ipady)
        
        self.file_dest_entry = tk.Entry(self.file_dest_lfm, text="폴더 선택", state=tk.DISABLED)
        self.file_dest_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        file_dest_btn = tk.Button(self.file_dest_lfm, text="찾아보기", width=10, command=self.dest_files)
        file_dest_btn.pack(side=tk.RIGHT)
        
    def file_opt(self):
        # Options
        file_opt_lfm = tk.LabelFrame(self.frm_merge, text="옵션", padx=self.padx, pady=self.pady)
        file_opt_lfm.pack(fill=tk.X, ipadx=self.ipadx, ipady=self.ipady)
        
        # Options - save file name
        file_opt_l_filename = tk.Label(file_opt_lfm, text="파일명")
        file_opt_l_filename.grid(column=0, row=0, padx=self.padx, pady=self.pady)
        self.file_opt_entry_filename = tk.Entry(file_opt_lfm, width=10, justify=tk.CENTER)
        self.file_opt_entry_filename.insert(0, "out")
        self.file_opt_entry_filename.grid(column=0, row=1, padx=self.padx, pady=self.pady)
        
        # Save & Next
        file_opt_fm_save_next = tk.Frame(self.frm_merge, padx=self.padx, pady=self.pady)
        file_opt_fm_save_next.pack(fill=tk.X, ipadx=self.ipadx, ipady=self.ipady)
        self.file_opt_btn_save = tk.Button(file_opt_fm_save_next, text="저장하기", width=20, command=self.save_files)
        self.file_opt_btn_save.pack(side=tk.RIGHT)
        
        
        
    # Controllers
    def add_files(self):
        dm = data_control.DataMgr()
        _files = dm.AddFiles()
        list_to_files = self.file_listbox_lb.get(0, tk.END)
        
        for file in _files:
            if file not in list_to_files:
                self.file_listbox_lb.insert(tk.END, file)
                
        if self.file_listbox_lb.size() > 0:
            self.file_control_btn_merge_file.config(state=tk.NORMAL)
            
    def del_files(self):
        for index in reversed(self.file_listbox_lb.curselection()):
            self.file_listbox_lb.delete(index)
            
        self.file_listbox_lb.selection_set(tk.END)
        self.df_merge = pd.DataFrame(data=None)
        
        if self.file_listbox_lb.size() == 0:
            self.file_control_btn_merge_file.config(state=tk.DISABLED)
            
    def dest_files(self):
        dm = data_control.DataMgr()
        _dest_dir = dm.GetDir()
        
        if _dest_dir == "":
            return
        else:
            self.file_dest_entry.config(state=tk.NORMAL)
            self.file_dest_entry.delete(0, tk.END)
            self.file_dest_entry.insert(0, _dest_dir)
            self.file_dest_entry.config(state=tk.DISABLED)
            
    def save_files(self):
        pop = popup_control.PopUp()
        
        if self.df_merge.size == 0:
            pop.warning("파일 저장", "저장할 데이터가 없습니다")
        elif len(str(self.file_dest_entry.get())) == 0:
            pop.warning("파일 저장", "저장할 경로를 선택하세요")
        else:
            dest = str(self.file_dest_entry.get()) + "/" + self.file_opt_entry_filename.get() + ".csv"
            if os.path.isfile(dest):
                pop.yes_no("파일 저장", "파일을 덮어쓸까요?")
                if pop.get_res():
                    self.df_merge.to_csv(dest, sep=",", encoding="utf-8-sig")
                    pop.info("파일 저장", "파일을 덮어썼습니다")
                else:
                    pop.warning("파일 저장", "파일명을 변경하세요")
                    self.file_opt_entry_filename.focus_set()
            else:
                self.df_merge.to_csv(dest, sep=",", encoding="utf-8-sig")
                pop.info("파일 저장", "파일을 저장했습니다")
                
    def merge_files(self):
        self.file_control_pgbar.start()
        dm = data_control.DataMgr()
        pop = popup_control.PopUp()
        list_to_files = self.file_listbox_lb.get(0, tk.END)
        try:
            self.df_merge = dm.Merge(self.df_merge, list_to_files)
            print(self.df_merge)
            self.file_control_pgbar.complete()
            pop.info("파일 합치기", "작업완료")
        except:
            pop.error("파일 합치기", "실패!")
            
        if pop.get_res():
            self.file_control_pgbar.clear()
            
    def preview_files(self):
        preview = preview_window.Preview(self.root, "preview_files", "미리보기", 640, 480)
        preview.df_preview(self.df_merge)