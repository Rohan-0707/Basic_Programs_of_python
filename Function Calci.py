# <!-- This code is designed by Mr. Rohan Kumar Bhoi -->
# <!-- GitHub : github.com/rohan-0707 -->
# <!-- Instagram : i_am_the_rohan_ -->
# <!-- Facebook : facebook.com/rohan.bhoi.07 -->
# <!-- Mail ID : rohanbhoi1546@gmail.com -->
# <!-- Linkdi : rohan-kumar-bhoi -->
# <!-- Twitter : @rohanbhoi07 -->

# ___________________________________________________________________________________________________________________

# Functions....

def addition(x,y):            # Difining an Function with Parameters/Arguments
    z = x + y
    print(f"Addition of {x} + {y} = {z}")
    print("")
    
def sub(x,y):
    z = x - y
    print(f"Subtraction of {x} - {y} = {z}")
    print("")
    
def multi(x,y):
    z = x * y
    print(f"Multiplication of {x} x {y} = {z}")
    print("")
    
def div(x,y):
    z = x / y
    print(f"Division of {x} / {y} = {z}")
    print("")
    
def mod(x,y):
    z = x % y
    print(f"Modulation of {x} % {y} = {z}")
    print("")
    
def fdiv(x,y):
    z = x // y
    print(f"Modulation of {x} // {y} = {z}")
    print("")
    
def intro():                            # Defining an Function without Parameters/Arguments
    print("")
    print("This Calculator is designed by Code Makes Rohan....")
    print("")


print("")
print("Simple Python Calculator...!")
print("")

intro()                               #Calling of Function...

print("-------------------------------------------------")
print("")
print("Calculator Menu")
print("")

print(" Addition        :       +")
print(" Subtraction     :       -")
print(" Multiplication  :       *")
print(" Division        :       /")
print(" Modulation      :       %")
print(" Floor Division  :       //")

print("")
print("-------------------------------------------------")
print("")

choice = input("Choose an Operation : ")
print("")

if(choice == "+" or choice == '-' or choice == '*' or choice == '/' or choice == '%' or choice == '//'):
    num1 = int(input("Enter 1st Number : "))
    print("")
    num2 = int(input("Enter second Number : "))
    print("")

    if(choice == '+'):
        addition(num1,num2)               # Addition() Function are called
        
    elif(choice == '-'):
        sub(num1,num2)                    # sub() Function are called
        
    elif(choice == '*'):
        multi(num1,num2)                  # multi() Function are called
        
    elif(choice == '/'):
        div(num1,num2)                    # div() Function are called
        
    elif(choice == '%'):
        mod(num1,num2)                    # mod() Function are called
        
    elif(choice == '//'):
        fdiv(num1,num2)                   # fdiv() Function are called
    
else:
    print("")
    print("Invalid Operation Selected..!!!")
    print("")
    print("Please Run the Program Again and Select Right Operation !")
    print("")
    



# <!-- ____________________________________________________________________________________________________________________________________________________
#                                                                          Thank You !
# ____________________________________________________________________________________________________________________________________________________ -->
# 


# Watch my video on Youtube to underastand the Program Properly....
# Link : www.youtube.com/@codemakesrohan
