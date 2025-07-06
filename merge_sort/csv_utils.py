from typing import TextIO
import numpy as np
import tempfile
import random
import string
import csv
import os



def generate_csv(csv_name:str, target_gb:float=0.01, key_column:str="id"):
    DIR = os.path.dirname(__file__)
    columns = [key_column, "name", "email"]

    csv_path = f'{DIR}/{csv_name}'

    row_id = 1
    target_bytes = int(target_gb * (1024 ** 3))
    with open(csv_path, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)                # Header

        while os.path.getsize(csv_path) < target_bytes:
            row = []

            row.append(str(row_id))
            
            name = ''.join(random.choices(string.ascii_letters, k=10))
            row.append(name.capitalize())
            
            email = ''.join(random.choices(string.ascii_lowercase, k=5)) + "@test.com"
            row.append(email)
            
            writer.writerow(row)                # Values
            row_id += 1

    print(f"Finished writing {row_id - 1} rows to '{csv_name}', reaching ~{target_gb} GB.")

def swap_ids(new_file: TextIO, old_file: TextIO, raw_swaps: np.ndarray):
    
    true_swaps = {} # {key=<new_id>: value=<old_id>}
    for id_1, id_2 in raw_swaps:

        old_id_1 = true_swaps.get(id_1, id_1)
        old_id_2 = true_swaps.get(id_2, id_2)

        true_swaps[id_1] = old_id_2
        true_swaps[id_2] = old_id_1
    
    true_swaps = {v: k for k, v in true_swaps.items()} # {key=<old_id>: value=<new_id>}

    old_data_reader = csv.reader(old_file)
    new_data_writer = csv.writer(new_file)
    for old_row in old_data_reader:
        old_row_id = int(old_row[0])
        new_data_writer.writerow([true_swaps.get(old_row_id, old_row_id)] + old_row[1:])
    # print("Swaped")

def count_file_lines(file_path: str) -> int:
    with open(file_path, 'r', encoding='UTF-8') as f:
        return sum(1 for _ in f) - 1  # exclude header

def shuffled_ids(csv_name: str):
    DIR = os.path.dirname(__file__)
    tmp_file_path = f'{DIR}/{csv_name}.tmp'
    ori_file_path = f'{DIR}/{csv_name}'
    
    num_rows = count_file_lines(ori_file_path)

    swap_rounds = int(num_rows*0.005)
    print(f'{swap_rounds=}')

    with \
        open(tmp_file_path, 'w', newline='', encoding='UTF-8') as tmp_file, \
        open(ori_file_path,     'r', newline='', encoding='UTF-8') as ori_file:
        
        reader = csv.reader(ori_file)
        writer = csv.writer(tmp_file)

        writer.writerow(reader.__next__())

        for _ in range(swap_rounds):
            raw_swaps = np.random.randint(1, num_rows, size=(10_000, 2))
        
            swap_ids(tmp_file, ori_file, raw_swaps)

        os.replace(tmp_file_path, ori_file_path)

if __name__ == '__main__':
    generate_csv('test.csv', target_gb=0.05)
    shuffled_ids('test.csv')