# CALCULATOR IN PYTHONNN
num1= float(input("enter first number:"))
num2=float(input("enter second numer:"))
operation= input("choose operation(+, -, *, /,**, %, //, sqrt, avg):")

if operation =="+":
    print("Addition:", num1+num2)

elif operation == "-":
    print("subraction:", num1-num2)

elif operation == "*":
    print("multiplication:", num1*num2)

elif operation == "/":
    if num2==0 and operation in ["/", "//"]:
        print("Error: Division by zero is not allowed.")
    else:
        print("division:", num1/num2)

elif operation == "**":
    print("Power:", num1**num2)

elif operation == "%":
    if num2==0:
        print("Error")
    else:
        print("modulus:", num1%num2)

elif operation == "//":
    if num2==0:
        print("Error")
    else:
        print("floor:", num1//num2)

elif operation == "sqrt":
    print("Square Root of num1:", num1**0.5)
    print("Square Root of num2:", num2**0.5)
elif operation == "avg":
    print("average:",(num1+num2)/2)

else:
    print("invalid operation")