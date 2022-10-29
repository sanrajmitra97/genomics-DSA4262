from os import listdir, mkdir
from os.path import isfile, join, exists

### Load Data
data_path = '../data/' #Update this line with dataset folder path
data_names = [k for k in listdir(data_path) if isfile(join(data_path, k))]
n_data = len(data_names)
for i in range(n_data):
    print(f"We are reading datafile {data_names[i]} which is associated with results_{i}")