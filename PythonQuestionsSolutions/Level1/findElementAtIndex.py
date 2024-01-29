# User function Template for python3
# Understand what happens when you use len(arr), n, n-1, len(arr)-1 in the loop
def findElementAtIndex(arr, n, key):
    # Your code goes here
    # print(len(arr))
    # print(n)
    # print("_________")
    for i in range(n):
        if i == key:
            return arr[i]
        else:
            continue
