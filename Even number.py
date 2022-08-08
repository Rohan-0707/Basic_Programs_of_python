# we need to declare our start and end point of the loop.
start = 1                           # here we declare a variable 'start' with value '1'
end = 10                            # same thing we again declare one more variable 'end' with value '10'

# we used a for loop to access all the numbers between 1 to 10
for i in range(start, end+1):       # here we declare one more variable 'i' to access the numbers betwwen 1 to 10,
                                    # by using the range method of python we set a range of for loop and passed the 'start' and 'end' as parameters of start and end point of range.
                                    # we increment end + 1 for accesing the last element of end, which is 10.
    if i % 2 == 0:                  # here we used if statement to check the number is even or not.
        print(i)
