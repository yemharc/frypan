import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdig

from Frypan_Controllers import window_control

class MergeWindow:
    def __init__(self, window, notebook):
        self.frm_merge = tk.Frame(window)
        window_control.SetPadding(self.frm_merge, 6, 6)
        notebook.add(self.frm_merge, text="파일 합치기")
        
        # File buttons
        _fm_btn = tk.Frame(self.frm_merge)
        _fm_btn.pack(fill="x")
        _btn_ins_file = tk.Button(_fm_btn,
                                    width=30,
                                    text="파일 추가",
                                    command=self.add_files)
        _btn_ins_file.pack(side="left")
        
        _btn_del_file = tk.Button(_fm_btn,
                                    width=30,
                                    text="파일 삭제",
                                    command=self.del_files)
        _btn_del_file.pack(side="left")
        
        _btn_run_file = tk.Button(_fm_btn,
                                    width=30,
                                    text="파일 합치기")
        _btn_run_file.pack(side="right")
        
        # File listbox & scrollbar
        _lfm_list = tk.LabelFrame(self.frm_merge, text="파일목록")
        _lfm_list.pack(fill="x")
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
        _lfm_dest_path = tk.LabelFrame(self.frm_merge, text="저장경로")
        _lfm_dest_path.pack(fill="x")
        
        _txt_dest_path = tk.Entry(_lfm_dest_path)
        _txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)
        
        _btn_dest_path = tk.Button(_lfm_dest_path, text="찾아보기", width=10)
        _btn_dest_path.pack(side="right")
        
        # Options
        _lfm_opts = tk.LabelFrame(self.frm_merge, text="옵션")
        _lfm_opts.pack(fill="x")
        
        opt_filetype = ["CSV", "xlsx"]
        _cmb_filetype = ttk.Combobox(_lfm_opts,
                                        state="readonly",
                                        values=opt_filetype,
                                        width=10,
                                        justify="center")
        _cmb_filetype.current(0)
        _cmb_filetype.pack(side="left")
        
        # Progress bar
        _frm_progress = tk.LabelFrame(self.frm_merge, text="진행상황")
        _frm_progress.pack(fill="x")
        
        _pgbar_value = tk.DoubleVar()
        _pgbar = ttk.Progressbar(_frm_progress, maximum=100, variable=_pgbar_value)
        _pgbar.pack(fill="x")
        
    def add_files(self):
        _files = window_control.AddFiles()
        list_to_files = self._lb_listbox.get(0, tk.END)
        for file in _files:
            if file not in list_to_files:
                self._lb_listbox.insert(tk.END, file)

    def del_files(self):
        for index in reversed(self._lb_listbox.curselection()):
            self._lb_listbox.delete(index)
        self._lb_listbox.selection_set(tk.END)