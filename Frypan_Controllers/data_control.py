import tkinter as tk
import tkinter.filedialog as fdig

import os
import pandas as pd
import chardet

class DataMgr:
    def __init__(self):
        self._ftypes = [("CSV","*.csv"), ("Excel",("*.xlsx","*.xls")),("Text","*.txt")]
        self._print_header = []
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def AddFiles(self):
        return fdig.askopenfilenames(title="파일을 선택하세요", filetypes=self._ftypes, initialdir=r"c:/dev")
    
    def AddFile(self):
        return fdig.askopenfilename(title="파일을 선택하세요", filetype=self._ftypes, initialdir=r"c:/dev")

    def GetDir(self):
        return fdig.askdirectory(title="폴더를 선택하세요", initialdir=r"c:/dev")
    
    def Merge(self, df, lists):
        df = pd.DataFrame(data=None)
        header = []
        
        for f in lists:
            with open(f, 'rb') as _file:
                execute = os.path.splitext(f)[1]
                encoding = chardet.detect(_file.read(1024)).get('encoding')

                if execute == ".csv":
                    df = (pd.read_csv(f, encoding=encoding) for f in lists)
                elif execute == ".xlsx" or execute == ".xls":
                    print("excel")
                    df = (pd.read_excel(f, sheet_name=0) for f in lists)
                elif execute == ".txt":
                    df = (pd.read_csv(f, encoding=encoding, sep="\s+") for f in lists)
                else:
                    pass
                
        df = (pd.concat(df, ignore_index=True))
        header = df.columns
        
        return df, header