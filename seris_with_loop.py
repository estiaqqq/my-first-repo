# s = ""
# i = 0
# j = 0
# n = 5

# while (i < n):
#     s = s + str(i) + "_"
#     # print("Value of S:", s, "value of i:", i)
#     i += 1

# # print(s)

s = ""
row = ""
col = ""
i = 1
j = 1
n = 5

while (i < n):
    while (j < n):
        s = s + str(j) + "_"
        row = row + "i:" + str(i) + " j:" + str(j) + " | "
        j += 1
    print(row)
    row = ""
    i += 1
    j = 1

print(s)

# | 1, 2, 3 |
# | 1, x, 3 |
# | 1, 2, 3 |

# * * *
# * *
# *
# * *
# * * *
