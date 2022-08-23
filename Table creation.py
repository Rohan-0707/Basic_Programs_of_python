# This code is developed by Mister Rohan Kumar Bhoi
# Instagram ID : i_am_the_rohan
# facebook : facebook.com/rohan.bhoi.07
# Mail ID : rohanbhoi1546@gmail.com
# My Blog : www.technicalrohan07.blogspot.com
# Linkdi : rohan-kumar-bhoi
# Twitter : Rohan_KumarBhoi

#   This is the code for Table Creation of any Number !
#   Here we can able to create any table of any any number !

a = 1                   # Here we create a variable 'a' for incremental object, which helps to multiply the number in range of 1 to 10
b = input("Enter The Number : ")    # This is our another variable, which takes a number from user to create their table !
for i in range(1,10+1):             # Here we used a for loop
    b = int(b)                      # Here we can convert the string value to number which taken from user !
    c = b * a                       # Here we create another variable 'c' for multiplying the number with incremental object
    a += 1                          # for incrementing the value of 'a' by 1, we used this formula
    print(c)                        # At the last we can print the last output of our table
