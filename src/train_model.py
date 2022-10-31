import pickle
from os import listdir, mkdir
from os.path import isfile, join, exists
from prep_data import preprocess
import rich.progress
import json
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, auc, precision_recall_curve


# Load data
data_path = '../data/train/'
data_names = [k for k in listdir(data_path) if isfile(join(data_path, k))]
# We know that X_train is a json file, so let us get those files. 
X_train_list = []
y_train_list = []
for file in data_names:
    if file[-4:] == 'json':
        X_train_list.append(file)
    else:
        y_train_list.append(file)

print('LOADING X TRAIN')
with rich.progress.open(data_path+X_train_list[0], "rb") as file:
    json_data = [json.loads(line) for line in file]
prep = preprocess(json_data)
X_train = prep.get_dataframe()

print('LOAD y TRAIN')
labels = pd.read_csv(data_path+y_train_list[0], sep=',')
y_train = prep.get_y_train(labels)
print('##################LOADING DATA COMPLETED##################')

# Train model
print('TRAIN MODEL')
cols_to_use = ['mean_lsd', 'mean_lm', 'var_lm', 'mean_csd', 'var_csd', 'mean_cm',
    'var_cm', 'mean_rsd', 'mean_rm', 'var_rm', 'num_reads', 'G_count',
    'T_count', 'relative_pos', 'order_1_A', 'order_1_T', 'order_2_A',
    'order_2_G', 'order_3_A', 'order_4_A', 'order_4_C', 'order_4_T',
    'order_5_A', 'order_5_G', 'order_5_T'] #xgb columns
X_train = X_train[cols_to_use].values
clf = XGBClassifier(n_estimators=85, eta=0.15, scale_pos_weight=4.9, max_depth=7)
clf.fit(X_train, y_train)
print('##################TRAINING MODEL COMPLETED##################')

# Results
print("PRINTING RESULTS")
def prauc_score(y_true, y_score):
    # Data to plot precision - recall curve
    precision, recall, thresholds = precision_recall_curve(y_true, y_score)
    # Use AUC function to calculate the area under the curve of precision recall curve
    auc_precision_recall = auc(recall, precision)
    return auc_precision_recall
final_y_score = clf.predict_proba(X_train)[:, 1]
print(f"Training AUCROC Score: {roc_auc_score(y_train, final_y_score)}")
print(f"Training PR AUC {prauc_score(y_train, final_y_score)}")

# save model
print('SAVING MODEL')
outdir = '../models'
model_name = input(f"Give the model a name:\n")
filename = f'/{model_name}.sav'
if not exists(outdir):
    mkdir(outdir)
pickle.dump(clf, open(outdir+filename, 'wb'))