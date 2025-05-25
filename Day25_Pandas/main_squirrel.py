import pandas as pd

# Operations
df = pd.read_csv('squirrel.csv', sep=',')

grey = len(df[df['Primary Fur Color'] == 'Gray'])
black = len(df[df['Primary Fur Color'] == 'Black'])
cinnamon = len(df[df['Primary Fur Color'] == 'Cinnamon'])
#
# df_furs = pd.concat([grey, black, cinnamon], ignore_index=True)
#
# groupedFur = df_furs.groupby('Primary Fur Color').count()['X']

#
# grouped = df.groupby('Primary Fur Color').count()['X']
# print(grouped)
# print(groupedFur)

data_dict = {
    'FurColor' : ['Grey', 'Black', 'Cinnamon'],
    'Count' : [grey, black, cinnamon]

}

df  = pd.DataFrame(data_dict)
print(df)