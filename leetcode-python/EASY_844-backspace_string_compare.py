# O(N) time, O(N) space complexity

# simulate stack and compare results.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_list = []
        ans1 = ""
        ans2 = ""
        
        for char in S:
            if char == '#':
                if stack_list:
                    stack_list.pop()
            else:
                stack_list.append(char)
        ans1 = ''.join(stack_list)
        
        stack_list = []
        for char in T:
            if char == '#':
                if stack_list:
                    stack_list.pop()
            else:
                stack_list.append(char)
        ans2 = ''.join(stack_list)
        
        if ans1 == ans2:
            return True
        else:
            return False
            
