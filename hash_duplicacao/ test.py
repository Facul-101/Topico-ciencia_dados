from hash_map import HashMap
import pandas as pd
import csv
import os

DIR = os.path.dirname(__file__)
KEY = 'id'  # pode ser 'cpf', 'email', etc

with open(DIR + f'/test.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)

    header = reader.__next__()

    hm = HashMap[str, dict](size=100)

    for row in reader:

        row_data = {}
        key: str
        for h, value in zip(header, row):

            if h == KEY:
                key = value
            else:
                row_data[h] = value

        hm.unique_insert(key, row_data)

print("Com duplicatas")
dupi = pd.read_csv(DIR + f'/test.csv')
print(dupi)

print('Sem duplicatas')
uniq = pd.DataFrame(list(hm))
print(uniq)

print(f"Total de registros originais: {len(dupi)}")
print(f"Registros únicos: {len(uniq)}")
print(f"Colisões detectadas: {hm.num_collisions}")
print(f"Duplicatas removidas: {hm.num_duplicates}")
