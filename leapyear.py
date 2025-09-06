year = int(input("enter year :"))
if year % 100 == 0:
    print("its not leapyer")
elif year % 4 == 0 or year % 400 == 0:
    print("its leapyer")
else:
    print("its not leapyer")
