class Solution:
    def combine(self, n: int, k: int):
        def bt(curr, start):
            if len(curr) == k:
                ans.append(curr[:])
                return
            for i in range(start, n+1):
                curr.append(i)
                bt(curr, i+1)
                curr.pop()

        ans = []
        bt([], 1)
        return ans
