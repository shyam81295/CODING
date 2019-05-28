# O(N) time, O(N) space compelxity

# push letters
# if last 3 letters is 'abc', pop all 3
# if stack is empty at the end, return True. Else return False.

class Solution:
    def isValid(self, S: str) -> bool:
        if len(S) <=2:
            return False
        stack_list = []
        for i,char in enumerate(S):
            stack_list.append(char)
            if len(stack_list) >= 3 :
                if stack_list[-3] == 'a' and stack_list[-2] == 'b' and stack_list[-1] == 'c':
                    a = stack_list.pop()
                    a = stack_list.pop()
                    a = stack_list.pop()
                    
        if not stack_list:
            return True
        else:
            return False
