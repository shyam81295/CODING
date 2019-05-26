# O(N) time complexity, O(N) space complexity
# smallest number after k digits is nothing but
# popping elements when you get smaller no. in list than stacktop element
# pop until k times, not necessarily it will be pop k elements in 1 go.

# corner cases:
# "17785", k = 4 | ans = "1"
# "10200", k = 1 | ans = "200"

# remove leading zeroes after creation of ans_string
# string is not empty, then we can use "str(int(..))" to remove leading zeroes.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        j = k
        ans_str ="0"
        stack_list = []
        while i <= len(num) - 1:
            if i>0 :
                while(len(stack_list) and int(num[i]) < int(stack_list[-1]) and j>0) :
                    j -= 1
                    a = stack_list.pop()
            stack_list.append(num[i])
            i += 1
            
        while j>0:
            j -= 1
            a = stack_list.pop()
        
        if stack_list:
            ans_str = "".join(stack_list)
            ans_str = str(int(ans_str))
        return ans_str
