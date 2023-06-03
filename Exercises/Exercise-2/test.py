import pandas as pd
import os

# Directory containing the CSV files
directory = 'B:\downloads'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Read and concatenate the CSV files
dfs = []
for file in csv_files:
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate the DataFrames
combined_df = pd.concat(dfs)

# Save the combined DataFrame as "final.csv"
combined_df.to_csv('B:\downloads\final.csv', index=False)

