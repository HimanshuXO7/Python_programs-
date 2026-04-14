while True:
    num1 = int(input("enter your number :"))
    num2 = int(input("enter your number :"))

    operation = input("enter your operator (+,-,*,/) :").strip()

    if operation == "+":
        result1 = num1+num2
        print()
        print("result is", result1)
        print()
        print("*******************")
        print()
    elif operation == "-":
        result2 = num1-num2
        print()
        print("result is", result2)
        print()
        print("*******************")
        print()
    elif operation == "*":
        result3 = num1*num2
        print()
        print("result is ", result3)
        print()
        print("*******************")
        print()
    elif  operation== "/":
        result4 = num1/num2
        print()
        print("result is", result4)
        print()
        print("*******************")
        print()
    else:
        print("error hai")
        print("*******************")
        print()
    choice = input("aur calculate karna hai? (y/n): ").strip().lower()
    print()

    if choice == "n":
        print("calculator band ho gaya 👋")
        break
