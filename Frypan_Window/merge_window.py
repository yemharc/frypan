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
        self.df_current = pd.DataFrame(data=None)
        self.df_header = []
        self.df_header_selected = []
        self.df_header_return = []
        self._chk_df_header = []
        self._chk_var = dict()
        
        self.file_control()
        self.file_listbox()
        self.file_dest()
        self.file_header()
        
        
        
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
            yscrollcommand=self.file_listbox_sc_list.set
        )
        self.file_listbox_lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_listbox_sc_list.config(command=self.file_listbox_lb.yview)
        
    def file_dest(self):
        self.file_dest_lfm = tk.LabelFrame(
            self.frm_merge,
            text="파일 저장",
            padx=self.padx,
            pady=self.pady
        )
        self.file_dest_lfm.pack(fill=tk.X, ipadx=self.ipadx, ipady=self.ipady)
        
        self.file_dest_entry = tk.Entry(self.file_dest_lfm, width=40, state=tk.NORMAL, justify=tk.CENTER)
        self.file_dest_entry.insert(0, "저장 경로를 선택하세요")
        self.file_dest_entry.config(state=tk.DISABLED)
        self.file_dest_entry.pack(side=tk.LEFT, fill=tk.X)
        
        file_dest_btn = tk.Button(self.file_dest_lfm, text="찾아보기", width=20, command=self.dest_files)
        file_dest_btn.pack(side=tk.LEFT)
        
        self.file_dest_entry_filename = tk.Entry(self.file_dest_lfm, width=20, justify=tk.CENTER)
        self.file_dest_entry_filename.insert(0, "out")
        self.file_dest_entry_filename.pack(side=tk.RIGHT)
        
        self.file_dest_btn_save = tk.Button(self.file_dest_lfm, text="저장하기", width=20, command=self.save_files)
        self.file_dest_btn_save.pack(side=tk.RIGHT)
        
    def file_header(self):
        self.file_header_lfm = tk.LabelFrame(
            self.frm_merge,
            text="데이터 항목",
            padx=self.padx,
            pady=self.pady
        )
        self.file_header_lfm.pack(fill=tk.BOTH, ipadx=self.ipadx, ipady=self.ipady)
        
        file_header_btn_select = tk.Button(self.file_header_lfm, text="전체선택", command=lambda:self.df_select_header_all(1))
        file_header_btn_select.pack(side=tk.LEFT)
        file_header_btn_deselect = tk.Button(self.file_header_lfm, text="전체해제", command=lambda:self.df_select_header_all(0))
        file_header_btn_deselect.pack(side=tk.LEFT)
        file_header_btn_refresh = tk.Button(self.file_header_lfm, text="데이터 갱신", command=lambda:threading.Thread(target=self.df_select_refresh(self.df_header_return)).start())
        file_header_btn_refresh.pack(side=tk.LEFT)
        
        self.file_header_fm = tk.Frame(self.frm_merge)
        self.file_header_fm.pack(fill=tk.BOTH, ipadx=self.ipadx, ipady=self.ipady)
        
        
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
        
        if self.df_current.size == 0:
            pop.error("파일 저장", "저장할 데이터가 없습니다")
        elif len(str(self.file_dest_entry.get())) == 0:
            pop.error("파일 저장", "저장할 경로를 선택하세요")
        elif len(str(self.file_dest_entry_filename.get())) == 0:
            pop.error("파일 저장", "저장할 파일명을 입력하세요")
        else:
            dest = str(self.file_dest_entry.get()) + "/" + self.file_dest_entry_filename.get() + ".csv"
            if os.path.isfile(dest):
                pop.yes_no("파일 저장", "파일을 덮어쓸까요?")
                if pop.get_res():
                    self.df_current.to_csv(dest, sep=",", encoding="utf-8-sig", index=False)
                    pop.info("파일 저장", "파일을 덮어썼습니다")
                else:
                    pop.warning("파일 저장", "파일명을 변경하세요")
                    self.file_dest_entry_filename.focus_set()
            else:
                self.df_current.to_csv(dest, sep=",", encoding="utf-8-sig", index=False)
                pop.info("파일 저장", "파일을 저장했습니다")
                
    def merge_files(self):
        self.file_control_pgbar.start()
        dm = data_control.DataMgr()
        pop = popup_control.PopUp()
        list_to_files = self.file_listbox_lb.get(0, tk.END)
        try:
            self.df_merge, self.df_header = dm.Merge(self.df_merge, list_to_files)
            # print(self.df_merge)
            print(self.df_header)
            self.df_select_header(self.file_header_fm, self.df_header)
            self.df_select_refresh(self.df_header)
            
            self.file_control_pgbar.complete()
            pop.info("파일 합치기", "작업완료")
        except:
            pop.error("파일 합치기", "실패!")
            
        if pop.get_res():
            self.file_control_pgbar.clear()
            
    def preview_files(self):
        preview = preview_window.Preview(self.root, "preview_files", "미리보기", 640, 480)
        preview.df_preview(self.df_current)
        
        
    def df_select_header(self, frame, header):
        _df_select_cv = tk.Canvas(frame)
        sc = tk.Scrollbar(frame, orient=tk.VERTICAL, command=_df_select_cv.yview)
        _f_header = tk.Frame(_df_select_cv)
        
        count = 0
        rows = 1
        
        for child in self.df_header:
            for c in range(3):
                if count < len(self.df_header):
                    self._chk_var[count] = tk.IntVar()
                    _chks = tk.Checkbutton(
                        _f_header,
                        text=self.df_header[count],
                        variable=self._chk_var[count],
                        command=lambda count=count:self.df_select_header_click(count, self.df_header),
                        onvalue=1,
                        offvalue=0
                        )
                    
                    _chks.select()
                    _chks.grid(column=c, row=rows, sticky=tk.W)
                    self.df_header_selected.append(_chks)
                    count += 1
            rows += 1
        
        _df_select_cv.create_window(0, 0, anchor=tk.NW, window=_f_header)
        _df_select_cv.update_idletasks()
        _df_select_cv.configure(scrollregion=_df_select_cv.bbox(tk.ALL), yscrollcommand=sc.set)
        
        sc.pack(side=tk.RIGHT, fill=tk.Y)
        _df_select_cv.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        
    def df_select_header_all(self, select):
        self.df_header_return = []
        tag = 0
        
        for i in self.df_header_selected:
            if select:
                i.select()
            else:
                i.deselect()
                
        for i in self.df_header_selected:
            if self._chk_var[tag].get():
                self.df_header_return.append(self.df_header[tag])
            tag += 1
        
    def df_select_header_click(self, i, header):
        self.df_header_return = []
        tag = 0
        
        for i in self.df_header_selected:
            if self._chk_var[tag].get():
                self.df_header_return.append(self.df_header[tag])
            tag += 1
            
        print(self.df_header_return)
        
    def df_select_refresh(self, header):
        self.df_current = pd.DataFrame(data=None, columns=header)
        for col in header:
            self.df_current[col] = self.df_merge[col].values
            
        print(self.df_current)