# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [number**2 for number in numbers]
#
# print(squared_numbers)

#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# result = [num for num in numbers if num % 2 == 0]
#
# print(result)


# numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# numbers_2 = [2, 5, 6, 7]
#
# result = [num for num in numbers_2 if num not in numbers_1]
# print(result)
#
# sentence = "What is Airspeed Velocity of an Unladen Swallow?"
#
#
# result = { word : len(word) for word in sentence.split() }
#
# # result = [word for word in sentence.split()]
# print(result)
weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday": 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24,
}

weather_f = {day : (temp_c * 9/5 + 32) for (day,temp_c) in weather_c.items()}



print(weather_f)


