# n = 0
# n = int(input())
# for i in range(0,n,1):
#     i = i+1
#     print(f"{i}" * i)
n = 5
# n = int(input())
i = 1
j = 1
output_str = ""
for i in range(1, n, 1):
    for j in range(1, i, 1):
        output_str = output_str + str(j)
    output_str = output_str + "\n"
print(output_str)
