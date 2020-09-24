import tkinter as tk
import tkinter.filedialog as fdig

import pandas as pd
import chardet

# import numpy as np
# import glob
# import os

# from Frypan_Controllers import idx_list

class DataMgr:
    def __init__(self):
        self._ftypes = [("Data Files (csv, xlsx, xls)", ("*.csv","*.xlsx","*.xls")),
           ("CSV","*.csv"),
           ("Excel",("*.xlsx","*.xls")),
            ("All Files","*.*")]
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def AddFiles(self):
        return fdig.askopenfilenames(title="파일을 선택하세요", filetypes=self._ftypes, initialdir=r"c:/dev")

    def GetDir(self):
        return fdig.askdirectory(title="폴더를 선택하세요", initialdir=r"c:/dev")
    
    def Merge(self, df, lists):
        df = pd.DataFrame()
        
        for f in lists:
            with open(f, 'rb') as encode:
                encoding = chardet.detect(encode.read(1024)).get('encoding')
                merge = (pd.read_csv(f, encoding=encoding) for f in lists)
        
        df = pd.concat(merge, ignore_index=True)
        print(df)

# # INDEX formatting start
# def get_data():
#     if devprep == 'eol':
#         # concat CSV files
#         df = concat_csv_files()
#         df.columns = df.columns[:0].tolist() + idx_list.idx_eol_list
        
#         # Sort by START-DATETIME
#         df.sort_values(by=['START-DATETIME'], ascending=[True])
        
#         # time-stamp
#         df['START-DATETIME'] = pd.to_datetime(df['START-DATETIME'], format='%y%m%d_%H%M%S')
#         df['END-DATETIME'] = pd.to_datetime(df['END-DATETIME'], format='%y%m%d_%H%M%S')
#     elif devprep == 'shaft':
#         print("Shaft!")
#         pass
        
#     return df
# # INDEX formatting end



# def save_data():
#     try:
#         if os.path.exists(fout):
#             os.remove(fout)
#             print("Delete",os.path.abspath(fout))
            
#         df.to_excel(fout, index=False, encoding=fencode)
#         print("Create",os.path.abspath(fout))
#     except:
#         print("Not enought DataFrame. Check devprep!!")
        
#     print("Done")