print("")
print("Simple Python Calculator...!")
print("")

print("-------------------------------------------------")
print("")
print("Calculator Menu")
print("")

print(" Addition        :       +     ")
print(" Subtraction     :       -     ")
print(" Multiplication  :       *     ")
print(" Division        :       /     ")
print(" Modulation      :       %     ")
print(" Floor Division  :       //    ")

print("")
print("-------------------------------------------------")
print("")

choice = input("Choose an Operation : ")
print("")

if choice == "+" or choice == "-" or choice == "*" or choice == "/" or choice == "%" or choice == "//":
    num1 = int(input("Enter First Number : "))
    print("")
    num2 = int(input("Enter Second Number : "))

    if(choice == '+'):
        result = num1 + num2
        print("")
        print(f"{num1} + {num2} = {result}")
        print("")

    elif(choice == '-'):
        result = num1 - num2
        print("")
        print(f"{num1} - {num2} = {result}")
        print("")
        
    elif(choice == '*'):
        result = num1 * num2
        print("")
        print(f"{num1} x {num2} = {result}")
        print("")
        
    elif(choice == '/'):
        result = num1 / num2
        print("")
        print(f"{num1} / {num2} = {result}")
        print("")
        
    elif(choice == '%'):
        result = num1 % num2
        print("")
        print(f"{num1} Mod {num2} = {result}")
        print("")
        
    elif(choice == '//'):
        result = num1 // num2
        print("")
        print(f"{num1} // {num2} = {result}")
        print("")
else:
    print("")
    print("Invalid Operation selected...!")
    print("")
