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
user_input_number = 5

while (i < (user_input_number*2 + 1)):
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

        while (j <= i - user_input_number):
            row = row + "* "
            j += 1
        print(row)
        row = ""
        j = 1

    i += 1
