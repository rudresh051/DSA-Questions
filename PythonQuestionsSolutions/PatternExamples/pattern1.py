# For N = 2 the pattern will be 
# 2 2 1 1
# 2 1

# For N = 3 the pattern will be 
# 3 3 3 2 2 2 1 1 1
# 3 3 2 2 1 1
# 3 2 1
def printPat(n):
    #Code here
    
    for i in range(n):
        # print(i, end=" ")
        for j in range(n,0,-1):
            print((str(n-j+1) + " ")*(n-i), end="")
        if i < n - 1:
            print("$", end=" ")  # Add $ after each row except the last one
        else:
            print("$")


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# } Driver Code Ends