import multiprocessing as mp
import numpy as np
import tqdm
from itertools import repeat
from multiprocessing import Process, Manager
from multiprocessing import Pool
import pandas as pd
import workers

num_process = mp.cpu_count()
print("Number of cpu: ", num_process)

employee_df = pd.read_csv('employee.csv', low_memory=False)
data_df = pd.read_csv('data.csv', low_memory=False)

data_df['date'] = pd.to_datetime(data_df['date'])

print(employee_df.head())
print(data_df.head())


# Get data
name_dict = {}
for index, row in employee_df.iterrows():
    name_dict[row['ecode']] = row['ename']

empcodes = []
empcodes.extend(list(data_df['employee_code'].unique()))

print(name_dict)
print(empcodes[:10])


num_partitions = num_process
manager = Manager()
d = manager.dict()
df_split = np.array_split(data_df, num_partitions)
pool = Pool(num_process)
shared_arg = repeat(d, num_partitions)
for _ in tqdm(pool.map(workers.process_rows, zip(shared_arg, df_split)), total=num_partitions):
    pass
pool.close()
pool.join()