# calculate index of next greater element

# O(N) time, O(N) space complexity with stack
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans_list = [-1]*len(T)
        stack_list = []
        if T:
            i = 0
            stack_list.append(0)
        # doStuff only when there is more than 2 elements.
        if len(T) > 1:
            i = 1
            while i < len(T):
                while stack_list and T[stack_list[-1]] < T[i]:
                    a = stack_list.pop()
                    ans_list[a] = i-a
                stack_list.append(i)
                i += 1
        while stack_list:
            a = stack_list.pop()
            ans_list[a] = 0
        return ans_list
        
# O(N) time, O(N) space complexity without stack
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        res = [0] * n
        
        for i in range(n - 2, -1, -1):
            k = i + 1
            
            while T[i] >= T[k] and res[k] > 0:
                k += res[k]
                    
            if T[k] > T[i]:
                res[i] = k - i
                
        return res
