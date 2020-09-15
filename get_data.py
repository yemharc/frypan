import pandas as pd
import numpy as np
import glob
import os

# custom columns
import idx_list

# devprep type : shaft, assm, eol
devprep = 'eol'
fout = 'output.xlsx'
fencode = 'utf-8-sig'

# concatenate CSV start
def concat_csv_files():
    path = r'./assets'
    all_files = glob.glob(os.path.join(path, "20*.csv"))
    df_all_file = (pd.read_csv(f, encoding='cp949') for f in all_files)
    return(pd.concat(df_all_file, ignore_index=True))
# concatenate CSV end

# INDEX formatting start
if devprep == 'eol':
    # concat CSV files
    eol_df = concat_csv_files()
    eol_df.columns = eol_df.columns[:0].tolist() + idx_list.idx_eol_list
    
    # Sort by START-DATETIME
    eol_df.sort_values(by=['START-DATETIME'], ascending=[True])
    
    # time-stamp
    eol_df['START-DATETIME'] = pd.to_datetime(eol_df['START-DATETIME'], format='%y%m%d_%H%M%S')
    eol_df['END-DATETIME'] = pd.to_datetime(eol_df['END-DATETIME'], format='%y%m%d_%H%M%S')
elif devprep == 'shaft':
    print("Shaft!")
# INDEX formatting end

try:
    if os.path.exists(fout):
        os.remove(fout)
        print("Delete",os.path.abspath(fout))
        
    eol_df.to_excel(fout, index=False, encoding=fencode)
    print("Create",os.path.abspath(fout))
except:
    print("Not enought DataFrame. Check devprep!!")
    
print("Done")