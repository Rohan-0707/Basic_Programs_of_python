#   Use of f-string

#   f-String : It is used to add any variables valus in any statement.

#   Starting of code...

print("")
a = "Rohan"

print(f"My name is {a}")
print("")

# Here we add the value of variable 'a' in a print Statement.

# How to use f-string:
#   1) In print() statement, before the double or single quotes, type f
#       Ex : print(f"")

#   2) After that type your Statement in Double or single Quotes.
#       Ex : print(f"My name  is : ")

#   3) After your statement in quotes add opening and closing curly brackets and type the variable name in between quotes.
#       Ex : a = "Rohan"
#           print(f"My name is : {a}")
#       Output : My name is : Rohan

#   Adding multiple variables in a single statement.

a = "Rohan"
b = 4
c = "TY"
d = 90.13

print("")
print(f"My name is {a}, My Roll NO is {b} and I am in {c} of Computer Engineering !")
print("")

#   Output : My name is Rohan, My Roll NO is 4 and I am in TY of Computer Engineering !

#   See, here we used multiple variables in a single statement by using the f-string !

print("")
print(f"Hello I am {a}, My Roll No is {b} and I was recently pass out my SY with {d}% marks, and now I am in {c}")
print("")