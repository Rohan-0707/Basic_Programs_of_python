# This is the code for Calculator Program in Python
print("")
print("This is the code of calculator program !")
print("")

# Starting of the program...

print("Choose an Operation for calculation !")
print("")
print("")

print("Type only First latter of any Operation to Proceed !")       # here the user are needs to type only the first letter of any operation.
print("")                                                           # Ex, For 'Addition' we need to type only 'A'.
print("")

print(" ----------------------- Menu ----------------------- ")
print("")
print(" ------->    Addition = A")
print(" ------->    Substraction = S")
print(" ------->    Multiplication = M")
print(" ------->    Division = D")
print("")
print(" ----------------------------------------------------- ")
print("")

print("Choose your Choice. Ex, if you want to Do Addition Type only A")
print("")
choice = input("Enter Your Choice : ")                  # Here we declare a variable 'choice' to take the operation from user.
print("")

a = input("Enter 1st Number : ")                        # Here we declare variable 'a' to take the 1st number from user.
print("")

b = input("Enter 2nd Number : ")                        # Same for the variable 'b'
print("")

a = int(a)                                              # Here we convert the value of the 'a' as string to integer
b = int(b)                                              # Same for variable 'b'

choice = choice.lower()                                 # To make the choice's all charater lower we used lower() method here.

if 'a' in choice:                                       # To check which operation is selected the user, we used if statement here.
    c = a + b
    print("")
    print("Your Addition is : "+str(c))

elif 's' in choice:
    c = a - b
    print("")
    print("Your Substraction is : "+str(c))

elif 'm' in choice:
    c = a * b
    print("")
    print("Your Multiplication : "+str(c))

elif 'd' in choice:
    c = a / b
    print("")
    print("Your Division is : "+str(c))

else:
    print("")
    print("Invalid Choice !!!!")                # When the user will choose any other choise instead of menu, the Error will Appears here.

print("")
print("Thaks For using our Calculator !")       # End of the Program...
print("")
