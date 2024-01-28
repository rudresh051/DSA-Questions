# Your task is to complete this function
# function should store the multiplication in C
def multiply(A, B, C, n):
    # Code here
    # print(A)
    # print(B)
    # print(C)
    for i in range(n):
        for j in range(n):
            curr_val = 0
            for k in range(2):
                curr_val = A[i][k]*B[k][j]
            C[i][j]=curr_val
    print(C)

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        matrix1 = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix1[i][j] = arr[c]
                c+=1
        arr = list(map(int, input().strip().split()))
        matrix2 = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix2[i][j] = arr[c]
                c+=1
        matrix3 = [[0 for i in range(n)]for j in range(n)]
        multiply(matrix1, matrix2, matrix3, n)
        for i in range(n):
            for j in range(n):
                print(matrix3[i][j], end=" ")
        print ('')
# Contributed By: Harshit Sidhwa

# } Driver Code Ends