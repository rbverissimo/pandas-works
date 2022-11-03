import pandas as pd

# create a dict with the info that will compose the DataFrame
entries = ['bot_1', 'Clever', 'bot_1', 'Renter', 'bot_1', 'Curious']
id_entries = ['001', '002', '001', '004', '001', '006']

entries_data = {'name': entries,
                'id': id_entries}

# create the dataframe and then generate a csv file
dataframe_entries = pd.DataFrame(entries_data)
dataframe_entries.to_csv('entries-duplicates.csv', index=False)
