def revStr (ob, S):
        # code here 
        rev = []
        size = len(S)
        for x in range(size-1,-1,-1):
            # print(S[x])
            rev.append(S[x])
        
        # print(rev)
        ans = "".join(rev)
        return ans