# Return true if str is binary, else false
def isBinary(str):
    # code here
    # print(type(str))
    result = [int(digits) for digits in str]
    # print(result)
    for i in range(len(result)):
        flag = False  # assuming result list only contains 0 and 1 digits
        if result[i] == 0 or result[i] == 1:
            flag = False
            continue
        elif result[i] != 0 or result[i] != 1:
            flag = True  # change the flag status to true which will indicate that the result list
            # has digits other than 0 and 1
            # if a digits is found other than 0 and 1 just break the loop and come out
            break

    # now based on flag condition just return 0 or 1
    if flag == False:
        return 1

    else:
        return 0
