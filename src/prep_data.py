import pandas as pd
import numpy as np

class preprocess():
    def __init__(self, data):
        self.data = data 
    def get_dataframe(self):
        transcripts = self.data.columns
        dataframes = []
        for transcript in transcripts:
            df_curr_transcript = self.data.loc[:, transcript]
            df_curr_transcript.dropna(inplace=True)
            df_curr_transcript = list(df_curr_transcript)
            
            for position in df_curr_transcript:
                #position here is a dictionary
                for k1, v1, in position.items():
                    order = list(v1.keys())[0]
                    for k2, v2 in v1.items():

                        
                        n = len(v2)

                        left_dwelling_t = np.zeros(n)
                        left_sd = np.zeros(n)
                        left_mean = np.zeros(n)

                        centre_dwelling_t = np.zeros(n)
                        centre_sd = np.zeros(n)
                        centre_mean = np.zeros(n)

                        right_dwelling_t = np.zeros(n)
                        right_sd = np.zeros(n)
                        right_mean = np.zeros(n)

                        for i in range(n):
                            left_dwelling_t[i] = v2[i][0]
                            left_sd[i] = v2[i][1]
                            left_mean[i] = v2[i][2]

                            centre_dwelling_t[i] = v2[i][3]
                            centre_sd[i] = v2[i][4]
                            centre_mean[i] = v2[i][5]
                            
                            right_dwelling_t[i] = v2[i][6]
                            right_sd[i] = v2[i][7]
                            right_mean[i] = v2[i][8]

                        left_dwelling_t_mean = np.mean(left_dwelling_t)
                        left_dwelling_t_var = np.var(left_dwelling_t)
                        left_sd_mean = np.mean(left_sd)
                        left_sd_var = np.var(left_sd)
                        left_mean_mean = np.mean(left_mean)
                        left_mean_var = np.var(left_mean)

                        centre_dwelling_t_mean = np.mean(centre_dwelling_t)
                        centre_dwelling_t_var = np.var(centre_dwelling_t)
                        centre_sd_mean = np.mean(centre_sd)
                        centre_sd_var = np.var(centre_sd)
                        centre_mean_mean = np.mean(centre_mean)
                        centre_mean_var = np.var(centre_mean)
                        
                        right_dwelling_t_mean = np.mean(right_dwelling_t)
                        right_dwelling_t_var = np.var(right_dwelling_t)
                        right_sd_mean = np.mean(right_sd)
                        right_sd_var = np.var(right_sd)
                        right_mean_mean = np.mean(right_mean)
                        right_mean_var = np.var(right_mean)

                        
                        
                    final_order = order[:3] + order[5:]
                    curr_dataframe = pd.DataFrame({'transcript_id':[transcript], 'order': [final_order], 'curr_pos': [k1], 
                                                'mean_ldt': [left_dwelling_t_mean], 'var_ldt':[left_dwelling_t_var], 'mean_lsd': [left_sd_mean], 'var_lsd': [left_sd_var], 'mean_lm':[left_mean_mean], 'var_lm': [left_mean_var], 
                                                'mean_cdt': [centre_dwelling_t_mean], 'var_cdt':[centre_dwelling_t_var] , 'mean_csd':[centre_sd_mean], 'var_csd': [centre_sd_var], 'mean_cm': [centre_mean_mean], 'var_cm': [centre_mean_var],  
                                                'mean_rdt': [right_dwelling_t_mean], 'var_rdt':[right_dwelling_t_var], 'mean_rsd': [right_sd_mean], 'var_rsd':[right_sd_var], 'mean_rm': [right_mean_mean], 'var_rm':[right_mean_var], 
                                                'num_reads': n})   
                    dataframes.append(curr_dataframe)
        final_df = pd.concat(dataframes)
        final_df['curr_pos'] = final_df['curr_pos'].astype('int64')
        final_df['A_count'] = final_df['order'].apply(lambda x: x.count('A'))
        final_df['C_count'] = final_df['order'].apply(lambda x: x.count('C'))
        final_df['G_count'] = final_df['order'].apply(lambda x: x.count('G'))
        final_df['T_count'] = final_df['order'].apply(lambda x: x.count('T'))
        final_df['relative_pos'] = final_df.groupby('transcript_id')['curr_pos'].rank()
        final_df['relative_pos'] = final_df['relative_pos'].astype(int)
        final_df['order_1'] = final_df['order'].apply(lambda x: x[0])
        final_df['order_2'] = final_df['order'].apply(lambda x: x[1])
        final_df['order_3'] = final_df['order'].apply(lambda x: x[2])
        final_df['order_4'] = final_df['order'].apply(lambda x: x[3])
        final_df['order_5'] = final_df['order'].apply(lambda x: x[4])
        
        #categorical data
        categorical_cols = ['order_1', 'order_2', 'order_3',
            'order_4', 'order_5']

        #import pandas as pd
        final_df = pd.get_dummies(final_df, columns = categorical_cols)
        return final_df 

