import pandas as pd
import pickle
from os import listdir, mkdir
from os.path import isfile, join, exists
from prep_data import preprocess


### Load Model
print('LOADING MODEL')
model_path = '../models/' #Update this line with model folder path
model_name = [f for f in listdir(model_path) if isfile(join(model_path, f))][0] # We assume there is just one model located in the model folder.
model = pickle.load(open(model_path+model_name, 'rb'))
print('##################LOADING MODEL COMPLETED##################')


### Load Data
print('LOADING DATA')
data_path = '../data/' #Update this line with dataset folder path
data_names = [k for k in listdir(data_path) if isfile(join(data_path, k))]
n_data = len(data_names)
data_frames = []
for i in range(n_data):
    # Send each json file for preprocessing. Get back a dataframe.
    data = pd.read_json(data_path+data_names[i], lines=True)
    prep = preprocess(data)
    prep_df = prep.get_dataframe()
    data_frames.append(prep_df)
print('##################LOADING DATA COMPLETED##################')



### Make predictions 
print('MAKING PREDICTIONS')

cols_to_use = ['mean_lsd', 'mean_lm', 'var_lm', 'mean_csd', 'var_csd', 'mean_cm',
    'var_cm', 'mean_rsd', 'mean_rm', 'var_rm', 'num_reads', 'G_count',
    'T_count', 'relative_pos', 'order_1_A', 'order_1_T', 'order_2_A',
    'order_2_G', 'order_3_A', 'order_4_A', 'order_4_C', 'order_4_T',
    'order_5_A', 'order_5_G', 'order_5_T'] #xgb columns


def make_predictions(data, model):
    df_submit = data.loc[:, ['transcript_id', 'curr_pos']]
    df_test = data[cols_to_use]
    score = model.predict_proba(df_test.values)[:, 1]
    df_submit['score'] = score
    df_submit['score'] = df_submit['score'].astype(float)
    df_submit = df_submit.rename(columns={'curr_pos':'transcript_position'})
    return df_submit

outdir = '../results'
for j in range(len(data_frames)):
    results = make_predictions(data_frames[j], model)
    outname = f'result_{j}.csv'
    if not exists(outdir):
        mkdir(outdir)
    results.to_csv(f"{outdir}/{outname}", index=False)
print('##################MAKING PREDICTIONS COMPLETED##################')
