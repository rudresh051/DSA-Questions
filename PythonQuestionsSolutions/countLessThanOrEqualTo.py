#Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.
def countOfElements( a, n, x):
    count = 0
    for number in a:
        # print(number)
        if number <= x:
            count = count+1
        else:
            continue
    
    return count