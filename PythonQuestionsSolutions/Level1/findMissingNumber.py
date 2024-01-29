def missingNumber(self, array, n):
    # code here
    arr1 = sorted(array)
    # print(array)
    # print(arr1)
    original = []
    for i in range(n):
        original.append(i + 1)
    # print(original)

    for val1, val2 in zip(arr1, original):
        if val1 == val2:
            continue
        else:
            return val2

    return original[len(original) - 1]
