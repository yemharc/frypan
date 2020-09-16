import pandas as pd
import numpy as np
import glob
import os

# custom columns
from Frypan_Controllers import idx_list

# devprep type : shaft, assm, eol
devprep = 'eol'
fout = 'output.xlsx'
fencode = 'utf-8-sig'
df = pd.DataFrame()

# concatenate CSV start
def concat_csv_files():
    path = r'./assets'
    all_files = glob.glob(os.path.join(path, "20*.csv"))
    df_all_file = (pd.read_csv(f, encoding='cp949') for f in all_files)
    return(pd.concat(df_all_file, ignore_index=True))
# concatenate CSV end



# INDEX formatting start
def get_data():
    if devprep == 'eol':
        # concat CSV files
        df = concat_csv_files()
        df.columns = df.columns[:0].tolist() + idx_list.idx_eol_list
        
        # Sort by START-DATETIME
        df.sort_values(by=['START-DATETIME'], ascending=[True])
        
        # time-stamp
        df['START-DATETIME'] = pd.to_datetime(df['START-DATETIME'], format='%y%m%d_%H%M%S')
        df['END-DATETIME'] = pd.to_datetime(df['END-DATETIME'], format='%y%m%d_%H%M%S')
    elif devprep == 'shaft':
        print("Shaft!")
        pass
        
    return df
# INDEX formatting end



def save_data():
    try:
        if os.path.exists(fout):
            os.remove(fout)
            print("Delete",os.path.abspath(fout))
            
        df.to_excel(fout, index=False, encoding=fencode)
        print("Create",os.path.abspath(fout))
    except:
        print("Not enought DataFrame. Check devprep!!")
        
    print("Done")