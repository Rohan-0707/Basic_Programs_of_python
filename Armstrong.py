# <!-- This code is designed by Mr. Rohan Kumar Bhoi -->
# <!-- GitHub : github.com/rohan-0707 -->
# <!-- Instagram : i_am_the_rohan_ -->
# <!-- Facebook : facebook.com/rohan.bhoi.07 -->
# <!-- Mail ID : rohanbhoi1546@gmail.com -->
# <!-- LinkdIn : rohan-kumar-bhoi -->
# <!-- Twitter : @rohanbhoi07 -->
# <!-- Whatsapp : http://bit.ly/3WVFh1W -->

# Armstrong Number Program in Python


print("")
print("")

print("Find Armstrong Number !")

print("")
print("")

num = int(input("Enter a Number : ")) 

print("")
print("")

temp = num
sum = 0
order = len(str(num))

while(num > 0):
    digit = num % 10
    sum = sum + digit ** order
    num = num // 10
    
if(sum == temp):
    print(f"{temp} is a Armstrong Number !")
    print("")
    print("")
else:
    print(f"{temp} is not a Armstrong Number !")
    print("")
    print("")
    
    
# <!-- ____________________________________________________________________________________________________________________________________________________
#                                                                          Thank You !
# ______________________________________________________________________________________________________________________________________________________ -->

