first = input("enter the first number : ")
operator = input("enter the operator (+,-,*,/,%) : ")
second = input("enter the second number : ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)    
else:
    print("invalid operation ")