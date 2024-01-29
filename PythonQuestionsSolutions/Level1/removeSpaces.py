class Solution:
    def modify(self, s):
        # code here
        y = s.strip()
        # print(y)
        arr = []
        for x in y:
            if x == " ":
                continue
            else:
                arr.append(x)

        arr1 = "".join(arr)
        return arr1
