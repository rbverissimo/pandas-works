import pandas as pd

tenants = ["Agmar", "Branca", "Danila", "Elaine", "Paulo"]

info_tenants = {'name': tenants,
                'rent': [330, 550, 550, 440, 550],
                'people living': [1, 2, 4, 3, 2]}

table_tenants = pd.DataFrame(info_tenants)

print(table_tenants)

# creating data from dataframe and adding it to the data frame
avg_per_person_living_rent = []
# avg = rent / people living
for i in range(len(table_tenants)):
    avg = table_tenants['rent'][i] / table_tenants['people living'][i]
    avg_per_person_living_rent.append(avg)

table_tenants["avg"] = avg_per_person_living_rent  # this line will add it to the data frame

print("After adding some new information to the data frame: ")
print(table_tenants)


