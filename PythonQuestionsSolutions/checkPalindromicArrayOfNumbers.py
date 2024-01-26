def PalinArray(arr, n):
    # Code here
    flag = False  # Assuming atlease one element of the array is not a palindrome
    for x in range(len(arr)):
        # Convert each element of the array in string
        y = str(arr[x])
        # print(y)
        # Now reverse the y
        y1 = y[::-1]
        # print(y1)
        if y1 == y:
            flag = (
                True  # Changing the flag status to true because element is a palindrome
            )
        else:
            flag = False
            break

    if flag == True:
        # so if in above code at last if get flag=True status that means every element in the array
        # was a palindrome
        return 1
    elif flag == False:
        return 0
