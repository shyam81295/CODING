class Solution:
    def generateParenthesis(self, n: int):
        def bt(curr, opens, closes, n, ans):
            if opens + closes == 2*n:
                ans.append(curr)
                return
            if opens < n:
                bt(curr+"(", opens+1, closes, n, ans)
            if closes < opens:
                bt(curr+")", opens, closes+1, n, ans)

        ans = []
        bt("", 0, 0, n, ans)
        return ans
