# User function Template for python3
class Solution:
    def removeVowels(self, S):

    # code here
    # 		res = []
    # 		res_without_vowel = []
    # 		for i in range(len(S)):
    # 		    res.append(S[i])
    # 	   # print("res",res)

    # 	    for i in range(len(res)):
    # 	        if res[i]=='a' or res[i]=='e' or res[i]=='i' or res[i]=='o' or res[i]=='u':
    # 	            continue
    # 	        else:
    # 	            res_without_vowel.append(res[i])
    #         # print("res_without_vowel",res_without_vowel)
    #         s1 = "".join(res_without_vowel)
    #         return s1

    # Method 2 - Optimized
        vowels = set('aeiou')
        res_without_vowel = []
        for character in S:
            if character not in vowels:
                res_without_vowel.append(character)
            else:
                continue

        return ''.join(res_without_vowel)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeVowels(s)

        print(answer)

# } Driver Code Ends