import pandas as pd

tenants = ["Agmar", "Branca", "Danila", "Elaine", "Paulo"]

info_tenants = {'name': tenants,
                'rent': [330, 550, 550, 440, 550],
                'people living': [1, 2, 4, 3, 2]}

table_tenants = pd.DataFrame(info_tenants)

print(table_tenants)
