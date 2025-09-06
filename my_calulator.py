print("wat u wanna do?")
oparator = input(":")
if oparator != "-" or oparator != "+" or oparator != "*" or oparator != "/":
    print("dats not oparetor")
    exit()
number1 = int(input("enter number1 :"))
number2 = int(input("enter number2 :"))
if oparator == "-":
    if number1 < number2:
        print("U R GAE")
    else:
        print(number1-number2)
elif oparator == "+":
    print(number1+number2)
elif oparator == "/":
    print(number1/number2)
elif oparator == "*":
    print(number1*number2)
else:
    print("dats not oparetor")
