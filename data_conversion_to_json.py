import pandas as pd

read_file = pd.read_excel(r'inventory_siea.xlsx')
print(read_file.to_json(r'inventory_siea.json'))

