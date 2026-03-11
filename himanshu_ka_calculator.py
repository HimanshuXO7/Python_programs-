num1 = int(input("enter your number :"))
num2 = int(input("enter your number :"))

operation = input("enter your operator (+,-,*,/):").strip()

if operation == "+":
    result1 = num1+num2
    print("result is", result1)
    
elif operation == "-":
    result2 = num1-num2
    print("result is", result2)
elif operation == "*":
    result3 = num1*num2
    print("result is ", result3)
elif  operation== "/":
    result4 = num1/num2
    print("result is", result4)
else:
    print("error hai")


