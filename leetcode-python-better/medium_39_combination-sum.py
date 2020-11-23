class Solution:
    def combinationSum(self, candidates, target):
        def bt(curr, start, curr_sum):
            if curr_sum == target:
                ans.append(curr[:])
                return
            if curr_sum > target:   # end the path
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                curr_sum += candidates[i]
                bt(curr, i, curr_sum)
                curr.pop()
                curr_sum -= candidates[i]

        ans = []
        bt([], 0, 0)
        return ans
