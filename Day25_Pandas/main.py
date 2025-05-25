import pandas as pd
from numpy.ma.extras import average

# with open('weather_data.csv', 'r+') as file:
#         file_list = [item.strip() for item in file.readlines()]
#         print(file_list)

# dataframe = pd.read_csv('weather_data.csv', sep=',')
# print(dataframe['temp'])
# print(list(dataframe['temp']))
#
#
# print(type(dataframe))
# print(type(dataframe['temp']))

#Operations
dataframe = pd.read_csv('weather_data.csv', sep=',')

# dict = dataframe.to_dict()
# json = dataframe.to_json()
# print(json)
#
# temps_avg = average(dataframe['temp'].tolist())
# print(round(temps_avg, 2))
#
# print(dataframe['temp'].mean())
#
# print(dataframe['temp'].max())
#
# print(dataframe.condition)

#Get the specific row
print(dataframe[dataframe['day'] == 'Monday'])

#Row with max temperature
print(dataframe[dataframe.temp == dataframe.temp.max()])

data_dict = {
    'students': ['Anish', 'Ruchi', 'Piyaa'],
    'scores' : [85,95,92]
}

df = pd.DataFrame(data_dict)
print(df.students)
df.to_csv('Anish.csv')
