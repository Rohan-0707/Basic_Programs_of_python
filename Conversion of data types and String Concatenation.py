# Type Casting and String Concatenation
# Conversion of the Integer values to String Values.
# Concatenation of two Strings

a = 10
b = 40

print("")
print(f"The Value of 'a' is : {a}")
print("")
print(f"The Value of 'b' is : {b}")
print("")
print("Now the value of 'a' is becomes string : "+str(a))       # Here we used str keyword to convert the value of 'a'
print("")

print("The actual addition of 'a' + 'b' is : ",int(a)+int(b))
print("")

a = str(a)              # See here we converted the value of int a to string
b = str(b)              # here we declare variavle 'a' as string of 'a' and variable 'b' as String 'b'

c = a + b               # here we add the value of 'a' and 'b' and stored their result in variable 'c'
#print("")
print("But we converted the values of 'a' and 'b' to string, so the 'a' + 'b' is : "+c)
print("")

print("We convert the values of 'a'  and 'b' as string, so the String Concatenation of 'a' + 'b' is becomes : "+c)
print("")

# Note : we cannot able concate the integer values

a = int(a)
b = int(b)

print("We again converted the values to Integer !")
print("")
print("Now see we cannot able to concate the integer values !")
print("")
print("when we tries to concate the the integer vaules we got errors like : ")
print("")
print("Concatenation of integer A and B is : "+a +b)

# Summury:

#        1) We can able to convert the datatype of any variable to another one
#           Ex : a = 10, a = str(a), a = float(a) 

#       2) If we convert any integer values to string,then their addition is becomes their string concatenation
#           Ex : a = 10, b = 40, c = str(a) + str(b), so the value of 'c' is becomes 1040. not 50 !

#       3) We cannot able to do any other arithematic operation on String

#       4) We can able to concate more than two strings easily
#           Ex : a = 1, b = 2, c = 3, d = 4, d = 5, e = 6,....
#               concate = str(a) + str(b) + str(c) + str(d) + str(e) + ......
#               print(concate)
#           Result : "123456...."

#       5) we can able to declare any variables names as in multiple datatypes
#           Ex : a = 10 | a = str(a) | a = float(a)


#   ____________________________________________________________________________________________________________________________________________________

#                                                                         Thank You !
#   ____________________________________________________________________________________________________________________________________________________

