import random
import pandas as pd
names = ['Anish', 'Piyu', 'Ruchi', 'Aanu']

scores_dict = {name: random.randint(1, 100) for name in names}
print(scores_dict)
# passed_students_dict= { item[0]: item[1] for item in scores_dict.items() if item[1] > 60}
# print(passed_students_dict)

passed_students_dict = {student: score for (student, score) in scores_dict.items() if score >= 60}
# print(passed_students_dict)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = { item: len(item) for item in sentence.split(" ")}
# print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#(temp_c * 9/5) + 32 = temp_f
weather_f = {key: (value*9/5)+32 for (key, value) in weather_c.items()}

# print(weather_f)


# Looping the Dataframe
data_dict = {
    'students': ['Anish', 'Ruchi', 'Piyaa'],
    'scores' : [85,95,92]
}

df = pd.DataFrame(data_dict)

for (index, row) in df.iterrows():
    print(index)
    print(row.students)
