# <!-- This code is designed by Mr. Rohan Kumar Bhoi -->
# <!-- GitHub : github.com/rohan-0707 -->
# <!-- Instagram : i_am_the_rohan_ -->
# <!-- Facebook : facebook.com/rohan.bhoi.07 -->
# <!-- Mail ID : rohanbhoi1546@gmail.com -->
# <!-- Linkdi : rohan-kumar-bhoi -->
# <!-- Twitter : @rohanbhoi07 -->


# Python Program to check an Number is Palidromeor not !

print("")               # Empty String !
print("")

num = int(input("Enter a Number : "))           # Typecating / Conversion of String to Number !
print("")
print("")
temp = num                                      # Temporary variable to store the actual value of variable num
reverse = 0                                     # Reverse variable to store the reverse of Number !

while(num > 0):                                 # While-Loop, it iterates a statement until, the condition goes wrong !
    digit = num%10                              # Digit variable forbreaking digits of a Number
    reverse = reverse * 10 + digit              # Logic to reverse a Number !
    num = num//10                               # Floar Division to get the exact division. Ex 5, 2,3, etc. not 5.1, 2.5, etc.
    
if(temp == reverse):                            # If statement to check the reverse is equals to temporary value/ Actual value
    print(f"{temp} is a Palindrome !")          # Use of F-String !
    print("")
    print("")
else:
    print(f"{temp} is not a Palindrome !")
    print("")
    print("")
    
    
# <!-- ____________________________________________________________________________________________________________________________________________________
#                                                                          Thank You !
# ______________________________________________________________________________________________________________________________________________________ -->

