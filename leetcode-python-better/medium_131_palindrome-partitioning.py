class Solution:
    def partition(self, s: str):
        def is_palindrome(start, end_plus_one):
            if s[start:end_plus_one] == s[start:end_plus_one][::-1]:
                return True
            return False

        def bt(curr, start):
            if start == len(s):
                ans.append(curr[:])
                return
            for i in range(start, len(s)):
                if is_palindrome(start, i+1):
                    curr.append(s[start:i+1])
                    bt(curr, i+1)
                    curr.pop()

        ans = []
        bt([], 0)
        return ans
