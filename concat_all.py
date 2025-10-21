import os
import pandas as pd

data_dir = r"PushshiftDumps-master\data"
all_dfs = []

for filename in os.listdir(data_dir):
    file_path = os.path.join(data_dir, filename)

    df = pd.read_csv(file_path, low_memory=False)
    all_dfs.append(df)

combined = pd.concat(all_dfs, ignore_index=True)

output_path = os.path.join(data_dir, r'comments.csv')
combined.to_csv(output_path, index=False)