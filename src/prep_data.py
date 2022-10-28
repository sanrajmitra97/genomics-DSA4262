import pandas as pd
import numpy as np
from tqdm import tqdm

class preprocess():
    def __init__(self, data):
        self.data = data
    def get_dataframe(self):
        all_rows = []
        for list_index in tqdm(range(len(self.data))):
            for gene_id in self.data[list_index]:
                for pos in self.data[list_index][gene_id]:
                    for bases in self.data[list_index][gene_id][pos]:
                        reads = self.data[list_index][gene_id][pos][bases]
                        avg_reads = [np.mean(x) for x in zip(*reads)]
                        variance_reads = [np.var(x) for x in zip(*reads)]
                        n_reads = [len(reads)]
                        one_row = [gene_id, int(pos), bases] + avg_reads + variance_reads + n_reads
                        all_rows.append(one_row)

        df = pd.DataFrame(all_rows, columns =['transcript_id', 'transcript_position', 'bases', 
        'mean_ldt', 'mean_lsd', 'mean_lm', 
        'mean_cdt', 'mean_csd', 'mean_cm',
        'mean_rdt', 'mean_rsd', 'mean_rm',
        'var_ldt', 'var_lsd', 'var_lm', 
        'var_cdt', 'var_csd', 'var_cm',
        'var_rdt', 'var_rsd', 'var_rm', 
        'num_reads'])


        df["order_1"] = df["bases"].apply(lambda x: x[0])
        df["order_2"] = df["bases"].apply(lambda x: x[1])
        df["order_3"] = df["bases"].apply(lambda x: x[2])
        df["order_4"] = df["bases"].apply(lambda x: x[5])
        df["order_5"] = df["bases"].apply(lambda x: x[6])
        df["A_count"] = df["bases"].apply(lambda x: x.count('A'))
        df["G_count"] = df["bases"].apply(lambda x: x.count('G'))
        df["C_count"] = df["bases"].apply(lambda x: x.count('C'))
        df["T_count"] = df["bases"].apply(lambda x: x.count('T'))
        categorical_cols = ['order_1', 'order_2', 'order_3', 'order_4', 'order_5']

        df = pd.get_dummies(df, columns = categorical_cols)
        df["relative_pos"] = df.groupby("transcript_id")["transcript_position"].rank()
        df["relative_pos"] = df["relative_pos"].astype(int)
        return df