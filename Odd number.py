print("Odd Numbers Program !")
print("")

# we need to declare our start and end point of the loop.
start = 1                           # here we declare a variable 'start' with value '1'
end = 10                            # same thing we again declare one more variable 'end' with value '10'

# we used a for loop to access all the numbers between 1 to 10
for i in range(start, end+1):       # here we declare one more variable 'i' to access the numbers betwwen 1 to 10,
                                    # by using the range method of python we set a range of for loop and passed the 'start' and 'end' as parameters of start and end point of range.
                                    # we increment end + 1 for accesing the last element of end, which is 10.
    if i % 2 != 0:                  # here we used if statement to check the number is odd or not.
        print(i)
print("")

# you can also use input function to get the start and end point from user using input() method.

print("")
print("this is the program for accesing the sart and end point to print the odd numbers betwwen two diferent numbers !")
print("")

start = input("Please enter the start number : ")
end = input("Please enter the end number : ")

# here we just need to convert the string values to integer values, by using typecasting method.

start = int(start)                  # we typrcast the string value of 'start' variable which is taken from the user to integer.
end = int(end)                      # we typrcast the string value of 'end' variable which is taken from the user to integer.

print("")

for i in range(start, end+1):
    if i % 2 != 0:                   # designing purpose
        print(i)
print("")