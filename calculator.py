num1 = float(input("please enyer first numberr\n"))
op = input("please enyer operator \n")
num2 = float( input("please enyer Second number \n"))

if op == "+":
    print("addition is ", (num1 + num2))
elif op == "-":
    print("Sub is ", ( num1-num2))
elif op == "/":
    print("division is ", ( num1/num2))
else:
    print ( "invalid operator ")
