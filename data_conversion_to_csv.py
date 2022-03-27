import pandas as pd

read_file=pd.read_excel(r'inventory_siea.xlsx')
read_file.to_csv(r'inventory_siea.csv', index=None,header=True)