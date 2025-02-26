import pandas as pd
import os

data_folder = "stackoverflow_data"
output_file = "_output/github_count.txt"
count = 0

csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith(".csv")]

for file in csv_files:
    try:
        df = pd.read_csv(file, dtype=str, on_bad_lines="skip")  
        count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {count}")

with open(output_file, "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")

