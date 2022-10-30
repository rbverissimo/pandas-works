import pandas as pd

tenants = ["Agmar", "Branca", "Danila", "Elaine", "Paulo"]

info_tenants = {'name': tenants,
                'rent': [330, 550, 550, 440, 550],
                'people living': [1, 2, 4, 3, 2]}

table_tenants = pd.DataFrame(info_tenants)

print(table_tenants)

select_column = table_tenants['name']
print(select_column)
select_row = table_tenants.iloc[0]['name']
print(select_row)

# creating data from dataframe and adding it to the data frame
avg_per_person_living_rent = []
# avg = rent / people living
for i in range(len(table_tenants)):
    avg = table_tenants['rent'][i] / table_tenants['people living'][i]
    avg_per_person_living_rent.append(avg)

table_tenants["avg"] = avg_per_person_living_rent  # this line will add it to the data frame

print("After adding some new information to the data frame: ")
print(table_tenants)

# saving it to csv
table_tenants.to_csv("tenants_avg.csv", index=False)  # saves it on the same path of the source
# table_tenants.to_csv("tenants_avg.csv", sep='\n')
# passing on an sep argument enables the code to define another separator other than a comma
# alo, even tho the to_csv is called to_csv it may also create files such as .txt




