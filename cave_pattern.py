# * * *
# * *
# *
# * *
# * * *

s = ""
row = ""
col = ""
i = 1
j = 1
user_input_number = 4

max_row = user_input_number * \
    2 - 1 if user_input_number % 2 == 0 else user_input_number * 2 - 1

print("max row - ", max_row)

while (i <= max_row):
    if (i < user_input_number):
        while (j <= (user_input_number - i + 1)):
            row = row + "* "
            j += 1
        print(row)
        row = ""
        j = 1

    elif (i == user_input_number):
        print("*")
    elif (i > user_input_number):

        while (j <= i - user_input_number + 1):
            row = row + "* "
            j += 1
        print(row)
        row = ""
        j = 1

    i += 1
