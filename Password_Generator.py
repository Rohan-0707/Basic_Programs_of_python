# <!-- This code is designed by Mr. Rohan Kumar Bhoi -->
# <!-- GitHub : github.com/rohan-0707 -->
# <!-- Instagram : i_am_the_rohan_ -->
# <!-- Facebook : facebook.com/rohan.bhoi.07 -->
# <!-- Mail ID : rohanbhoi1546@gmail.com -->
# <!-- Linkdi : rohan-kumar-bhoi -->
# <!-- Twitter : @rohanbhoi07 -->


#Here we used the random() method of the python to generate a random password !
import random

#Here we created  list of chracters for the password !
pass1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
         "n","o","p","q","r","s","t","u","v","w","x","y","z",
         "A","B","C","D","E","F","G","H","I","J","K","L","M",
         "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
         "!","@","#","$","%","^","&","*","(",")","_","+","{",
         "}",":",","<",">","/",'",";","[","=","-",",","`","~",
         "`","1","2","3","4","5","6","7","8","9","0"]

# By using the input method, we get the lenth of the password form the user.
charLength = input("\nEnter the length of the password : ")

# declaring the empty string 
password = ""

#loop  to generate the random password of the length entered by the user
# Logic !
for x in range(int(charLength)):                      # Here we used our chaLength variable in the form of Integers by using typecasting !
    password = password + random.choice(pass1)[0]
    


print("\nYour new Password is : "+password+"\n")


# <!-- ____________________________________________________________________________________________________________________________________________________
#                                                                          Thank You !
# ____________________________________________________________________________________________________________________________________________________ -->
