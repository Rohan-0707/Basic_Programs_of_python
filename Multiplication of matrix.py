# <!-- This code is designed by Mr. Rohan Kumar Bhoi -->
# <!-- GitHub : github.com/rohan-0707 -->
# <!-- Instagram : i_am_the_rohan_ -->
# <!-- Facebook : facebook.com/rohan.bhoi.07 -->
# <!-- Mail ID : rohanbhoi1546@gmail.com -->
# <!-- Linkdi : rohan-kumar-bhoi -->
# <!-- Twitter : @rohanbhoi07 -->

def Multiply(A,B):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    
    #for rows 
    for i in range(len(A)):
        #for columns 
        for j in range(len(B[0])):
            #for rows of matrix 8
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
                
    for p in result:
        print(p)
    return 0

A = [[1,2,3],[6,7,4],[8,10,11]]
B = [[1,5,3],[2,6,5],[7,4,9]]

print("\nResult : \n")
Multiply(A,B)
print("\n")

# <!-- ____________________________________________________________________________________________________________________________________________________
#                                                                          Thank You !
# ____________________________________________________________________________________________________________________________________________________ -->
