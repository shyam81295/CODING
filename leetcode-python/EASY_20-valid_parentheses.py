# stack solution
# O(N) time, O(N) space complexity
# insert chars into stack
# if closing bracket and its previous element is not matching opening bracket, then return False
# if newstack is not empty at the end, then return False.

class Solution:
    def isValid(self, s: str) -> bool:
        newstack = []
        answer = True
        for char in s:
            if char == ')':
                if len(newstack) > 0: 
                    x = newstack[-1]
                    newstack.append(char)
                    if x == '(':
                        y = newstack.pop()
                        y = newstack.pop()
                else:
                    answer = False
                    break
            elif char == ']':
                if len(newstack) > 0: 
                    x = newstack[-1]
                    newstack.append(char)
                    if x == '[':
                        y = newstack.pop()
                        y = newstack.pop()
                else:
                    answer = False
                    break
            elif char == '}':
                if len(newstack) > 0: 
                    x = newstack[-1]
                    newstack.append(char)
                    if x == '{':
                        y = newstack.pop()
                        y = newstack.pop()
                else:
                    answer = False
                    break
            
            else:
                newstack.append(char)
                
        if len(newstack):
            answer = False
            
        return answer
            
