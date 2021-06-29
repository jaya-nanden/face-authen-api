import pandas as pd
from spreadsheet_update import append_data, read_data


# Creating the column
# append_data(["status", "emotion"])

# Appending the data
# append_data(["yes", "happy"])
# append_data(["yes", "sad"])
# append_data(["yes", "angry"])


# Reading the data
# df = read_data()
# count_dict = df['emotion'].value_counts().to_dict()
# print(count_dict)


emotion_dict = {"Angry": 0, "Disgusted": 0, "Fearful": 0, "Happy": 0, "Neutral": 0 , "Sad": 0,  "Surprised": 0, "IDK": 0}
# keys = list(emotion_dict.keys())
# values = list(emotion_dict.values())
# print(keys)
# print(values)
df = read_data()

count_dict = df['emotion'].value_counts().to_dict()

for key, value in count_dict.items():
    emotion_dict[key] = value

# print(emotion_dict)