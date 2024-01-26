class Solution:
    def findIndex(self, a, N, key):
        b = []
        if key not in a:
            return -1, -1
        for i in range(N):
            if a[i] == key:
                b.append(i)
        return min(b), max(b)
