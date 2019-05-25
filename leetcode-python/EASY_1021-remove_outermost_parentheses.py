# O(N) time, O(N) space complexity
# outermost parentheses -> when stack is empty, note popped index & current index into a list of tuple
# then exclude those characters which belongs to that tuple.

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans_list = []
        stack_list = []
        ans_str = ""
        
        i=0
        while i<= len(S)-1:
            if S[i]==')':
                a = stack_list.pop()
                if not len(stack_list):
                    ans_list.append((a,i))
            else:
                stack_list.append(i)
            i += 1
        
        for ans in ans_list:
            x,y = ans
            ans_str = ans_str + S[x+1:y]
        return ans_str
