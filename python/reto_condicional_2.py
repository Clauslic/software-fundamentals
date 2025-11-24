print("Enter the number 1 ")
num1 = float(input())
print("Enter the number 2")
num2 = float(input())
if num1 > 0:
    if num1 % 2 == 0:
        print("The first number  " + str(num1) + " it's even")
    else:
        print("The first number  " + str(num1) + " It's odd")
else:
    if -num1 % 2 == 0:
        print("The first number  " + str(num1) + " it's even")
    else:
        print("The first number " + str(num1) + " It's odd")
if num2 > 0:
    if num2 % 2 > 0:
        print("The second number  " + str(num2) + " It's odd")
    else:
        print("The second number " + str(num2) + " it's even")
else:
    if -num2 % 2 > 0:
        print("The second number  " + str(num2) + " It's odd")
    else:
        print("The second number  " + str(num2) + " it's even")
