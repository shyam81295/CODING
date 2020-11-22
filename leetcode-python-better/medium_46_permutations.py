from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        def bt(curr, counter):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for elem in counter:
                if counter[elem] > 0:
                    curr.append(elem)
                    counter[elem] -= 1
                    bt(curr, counter)
                    curr.pop()
                    counter[elem] += 1

        nums.sort()
        ans = []
        bt([], Counter(nums))
        return ans
