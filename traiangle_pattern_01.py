n = 4
# n = int(input())
output_str = ""
i = 1
j = 1

while (i <= n):
    while (j <= i):
        output_str = output_str + str(j)
        j += 1
    output_str += "\n"
    j = 1
    i += 1


print(output_str)
