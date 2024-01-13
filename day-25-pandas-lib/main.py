# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1].isdigit():
#             temp.append(int(row[1]))
#         print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
# Create a table just like in csv file
temp = data["temp"].tolist()
# Create a list from value of a column
average = data["temp"].mean()
# Get average value from the value of a column
max_num = data["temp"].max()
# Get max value from the value of a column

data["condition"]
data.condition
# 2 way to access the value of a column in table (case-sensitive)


# print(data[data.temp == data.temp.max()])
# Get data in a row in data

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"{monday_temp_F}'F  ")
# Trans from 'C to 'F


# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "score":[76, 64, 77]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
# Create a dataframe from scratch and create new csv file to export data


