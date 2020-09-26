import tkinter as tk
import tkinter.filedialog as fdig

import os
import pandas as pd
import chardet
# from Frypan_Controllers import idx_list

class DataMgr:
    def __init__(self):
        self._ftypes = [("CSV","*.csv"), ("Excel",("*.xlsx","*.xls")),("Text","*.txt")]
        
    def __del__(self):
        print("delete instance : ", __name__)
        
    def AddFiles(self):
        return fdig.askopenfilenames(title="파일을 선택하세요", filetypes=self._ftypes, initialdir=r"c:/dev")

    def GetDir(self):
        return fdig.askdirectory(title="폴더를 선택하세요", initialdir=r"c:/dev")
    
    def Merge(self, df, lists):
        df = pd.DataFrame(data=None)
        
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
                
        return (pd.concat(df, ignore_index=True))

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