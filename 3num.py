number1 = int(input("enter number1 :"))
number2 = int(input("enter number2 :"))
number3 = int(input("enter number3 :"))
if number1 > number2 and number1 > number3:
    print("1 is biggest")
elif number1 < number2 and number2 > number3:
    print("2 is biggest")
else:
    print("3 is biggest")