#write a calculator program that endlessly prompts for input, until the user enters"0" instead of +,-,/,*

#set 4 functions for 4 operators(+,-,*,/)
def summa(a, b):
    return a+b

def diff(a, b):
    return a-b

def product_num(a, b):
    return a*b

def division(a, b):
    if b != 0:
        return a/b
    else:
        return ("Zero division error!")

#start an infinite loop that will be interrapted by entering "0" instead of (+,-,*,/)
while True:
    a = int(input("Enter Number1: "))
    b = int(input("Enter Number2: "))
    symbol = input("Enter the sign of the operation (+,-,/,*): ")
    if symbol == "+":
        print(summa(a,b))
    elif symbol == "-":
        print(diff(a,b))
    elif symbol == "*":
        print(product_num(a,b))
    elif symbol == "/":
        print(division(a,b))
    elif symbol == "0":
        break

