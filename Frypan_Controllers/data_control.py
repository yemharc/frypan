import tkinter as tk
import tkinter.filedialog as fdig

import os
import pandas as pd
import chardet

class DataMgr:
    def __init__(self):
        self._ftypes = [("CSV","*.csv"), ("Excel",("*.xlsx","*.xls")),("Text","*.txt")]
        self._print_header = []
        self.dest = os.getcwd() + '/output'
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def AddFiles(self):
        if not os.path.isdir(self.dest):
            os.mkdir(self.dest)
        return fdig.askopenfilenames(title="파일을 선택하세요", filetypes=self._ftypes, initialdir=self.dest)
    
    def AddFile(self):
        if not os.path.isdir(self.dest):
            os.mkdir(self.dest)
        return fdig.askopenfilename(title="파일을 선택하세요", filetype=self._ftypes, initialdir=self.dest)

    def GetDir(self):
        if not os.path.isdir(self.dest):
            os.mkdir(self.dest)
        return fdig.askdirectory(title="폴더를 선택하세요", initialdir=self.dest)
    
    def GetMaxCols(self, f):
        data_file_delimiter = ","
        largest_column_count = 0
        with open(f, 'r') as temp_f:
            lines = temp_f.readlines()

            for l in lines:
                column_count = len(l.split(data_file_delimiter)) + 1
                largest_column_count = column_count if largest_column_count < column_count else largest_column_count
        temp_f.close()
        
        column_names = [i for i in range(0, largest_column_count)]
        return column_names