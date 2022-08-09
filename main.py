print("Calculator\n")
print("What do you want to do?: ")
operators = ["+", "-", "*", "/", "%"]
print(*operators)

Calculation = input()

def addition():
    print("What is the first number you wish to add?")
    number1 = int(input())
    print("and")
    number2 = int(input())
    print("That equals = " + str("{:,}".format((number1 + number2))))

def subtract():
    print("What is the first number you wish to subtract?")
    number1 = int(input())
    print("subtracted from")
    number2 = int(input())
    print("That equals = " + str("{:,}".format((number1 - number2))))

def multiply():
    print("What is the first number you wish to multiply?")
    number1 = int(input())
    print("multiplied by")
    number2 = int(input())
    print("That equals = " + str("{:,}".format((number1 * number2))))

def divide():
    print("What is the first number you wish to divide?")
    number1 = int(input())
    print("divided by")
    number2 = int(input())
    print("That equals = " + str(round(number1 / number2, 3)))

def modulus():
    print("What is the first number you want?")
    number1 = int(input())
    print("and")
    number2 = int(input())
    print("That equals = " + str("{:,}".format((number1 % number2))))

try:
    while True:
        if Calculation == "+":
            addition()
            print("")
            again = input("Do you need to calculate something else? If yes type 'Yes' if no type 'Exit'")
            if again == "Yes":
                print(*operators)
                Calculation = input()
            elif again =="Exit":
                break
            else:
                break
        elif Calculation == "-":
            subtract()
            print("")
            again = input("Do you need to calculate something else? If yes type 'Yes' if no type 'Exit'")
            if again == "Yes":
                print(*operators)
                Calculation = input()
            elif again =="Exit":
                break
            else:
                break
        elif Calculation == "*":
            multiply()
            print("")
            again = input("Do you need to calculate something else? If yes type 'Yes' if no type 'Exit'")
            if again == "Yes":
                print(*operators)
                Calculation = input()
            elif again =="Exit":
                break
            else:
                break
        elif Calculation == "/":
            divide()
            print("")
            again = input("Do you need to calculate something else? If yes type 'Yes' if no type 'Exit'")
            if again == "Yes":
                print(*operators)
                Calculation = input()
            elif again =="Exit":
                break
            else:
                break
        elif Calculation == "%":
            modulus()
            print("")
            again = input("Do you need to calculate something else? If yes type 'Yes' if no type 'Exit'")
            if again == "Yes":
                print(*operators)
                Calculation = input()
            elif again =="Exit":
                break
            else:
                break
except ValueError:
    print("Please enter only numbers")