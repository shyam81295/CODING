class Solution:
    def subsets(self, nums):
        # helper function has access to nums function argument and
        # function variable 'ans'
        def helper(step, idx):
            if idx == len(nums):
                # since we are appending, and `ans` is mutable object,
                #   so it reflects change.
                # this is called as call by object reference.
                ans.append(step[:])
                return
            candidates = [True, False]
            for elem in candidates:
                if elem:
                    step.append(nums[idx])
                helper(step, idx+1)
                if elem:
                    step.pop()
        ans = []
        helper([], 0)
        return ans
