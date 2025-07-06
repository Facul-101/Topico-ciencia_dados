from typing import Literal, TypeAlias, TextIO, Sequence
from math import ceil
import shutil
import csv
import os

ORDER: TypeAlias =  Literal['desc', 'asc']

def ext_merge_sort(file_path: str, key_column: str | int, order: ORDER='asc'):
    valid_file_path = validate_path(file_path)

    with open(valid_file_path, newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        header = reader.__next__()
        key_index = header.index(key_column) if isinstance(key_column, str) else key_column

    run_paths = split_csv_run_files(valid_file_path, key_index)
    merge_sort_run_files(run_paths, key_index, order)
    merge_sorted_runs(valid_file_path, run_paths, key_index,  order)

def validate_path(file_path: str) -> str:
    assert isinstance(file_path, str)
    
    if os.path.isfile(file_path):
        return file_path
    
    DIR = os.path.dirname(__file__)
    new_path = f'{DIR}/{file_path}'

    if os.path.isfile(new_path):
        return new_path
    
    raise FileNotFoundError(f'File could not be found: {file_path}')

def split_csv_run_files(file_path: str, key_index: int) -> list[str]:
    
    chunk_size = 100_000

    DIR = os.path.dirname(file_path)
    NAME = os.path.basename(file_path)
    new_path = f'{DIR}/temp/{NAME}'
    os.makedirs(os.path.dirname(new_path), exist_ok=True)

    chunk = []
    run_paths = []
    with open(file_path, newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        header = reader.__next__()

        for i, row in enumerate(reader):
            chunk.append(row)
        
            if (i + 1) % chunk_size == 0:
                idx = ceil((i + 1)/chunk_size)

                run_path = f'{new_path}_{idx}.tmp'
                with open(run_path, 'w+', encoding='UTF-8') as run:
                    writer = csv.writer(run)

                    writer.writerow(header)
                    writer.writerows(chunk)
                
                run_paths.append(run_path)
                chunk.clear()

        if chunk:
            idx = ceil((i + 1)/chunk_size)
            chunk.sort(key=lambda x: x[key_index])

            run_path = f'{new_path}_{idx}.tmp'
            with open(run_path, 'w', encoding='UTF-8') as run:
                writer = csv.writer(run)

                writer.writerow(header)
                writer.writerows(chunk)
            
            run_paths.append(run_path)
    
    return run_paths

def merge_sort_run_files(run_paths: list[str], key_index: int, order: ORDER):

    for run_path in run_paths:
        
        with open(run_path, 'r', newline='', encoding='UTF-8') as tmp_file:

            reader = csv.reader(tmp_file)
            header = reader.__next__()

            lines = [line for line in reader]
            sorted_lines = merge_sort_run(lines, key_index, order)
        
        with open(run_path, 'w', encoding='UTF-8') as tmp_file:

            writer = csv.writer(tmp_file)
            writer.writerow(header)
            writer.writerows(sorted_lines)

def merge_sort_run(lista: list[list[str]], key_index: int, order: ORDER) -> list[list[str]]:

    if order == 'asc':
        ax = 1
    else:
        ax = -1

    if len(lista) > 1:

        meio = len(lista)//2

        lista_esquerda = lista[:meio]
        lista_direita = lista[meio:]

        merge_sort_run(lista_esquerda, key_index, order)
        merge_sort_run(lista_direita, key_index, order)

        i = 0
        j = 0
        k = 0

        while i < len(lista_esquerda) and j < len(lista_direita):

            if ax*int(lista_esquerda[i][key_index]) < ax*int(lista_direita[j][key_index]):
                lista[k] = lista_esquerda[i]
                i += 1
            else:
                lista[k] = lista_direita[j]
                j += 1
            k += 1

        while i < len(lista_esquerda):

            lista[k] = lista_esquerda[i]
            i += 1
            k += 1

        while j < len(lista_direita):
            lista[k] = lista_direita[j]
            j += 1
            k += 1
    
    return lista

def merge_sorted_runs(file_path: str, run_paths: list[str], key_index: int, order: ORDER):
    
    try:
        files = [open(run, 'r', newline='', encoding='utf-8') for run in run_paths]

        make_sorted_file(file_path, files, key_index, order)

        shutil.rmtree(os.path.dirname(file_path) + '/temp')

    finally:
        for file in files:
            file.close()

def make_sorted_file(file_path: str, files: Sequence[TextIO], key_index: int, order: ORDER):

    if order == 'asc':
        fo = min
    else:
        fo = max

    readers = [csv.reader(f) for f in files]
    for reader in readers:
            header = reader.__next__()

    new_path = file_path[:-4] + '_sorted.csv'

    with open(new_path, 'w', encoding='utf-8') as sorted_file:
        
        writer = csv.writer(sorted_file)
        writer.writerow(header)

        rows = []
        for reader in readers:
            row = reader.__next__()
            rows.append(row)

        while readers:

            chosen_row_id = rows.index(fo(rows, key=lambda x: int(x[key_index])))
            chosen_row = rows[chosen_row_id]

            writer.writerow(chosen_row)

            try:
                new_row = readers[chosen_row_id].__next__()
                rows[chosen_row_id] = new_row
            except StopIteration:
                readers.pop(chosen_row_id)
                rows.pop(chosen_row_id)

if __name__ == '__main__':
    ext_merge_sort('test.csv', 'id', 'asc')