import numpy as np
import wfdb
import tqdm
# import ast 
# import pandas as pd

def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in tqdm.tqdm(df.filename_lr)]
    else:
        data = [wfdb.rdsamp(path+f) for f in tqdm.tqdm(df.filename_hr)]
    data = np.array([signal for signal, meta in data])
    return data

# path = "data/raw/ptb-xl-1.0.3/"
# sampling_rate = 100

# Y = pd.read_csv(path + "ptbxl_database.csv", index_col='ecg_id')
# Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

# X = load_raw_data(Y, sampling_rate, path)