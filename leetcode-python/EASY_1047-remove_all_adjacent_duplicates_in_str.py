# O(N) time, O(N) space complexity
# put the characters in stack, pop both if both adjacent elements are matching 
# else keep it in stack
# remaining chars in stack is the answer.

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack_list = []
        ans_str = ""
        i = 0
        while i <= len(S)-1 :
            stack_list.append(S[i])
            if len(stack_list) >= 2:
                a = stack_list.pop()
                b = stack_list.pop()
                if a != b:
                    stack_list.append(b)
                    stack_list.append(a)
            i += 1
            
        return "".join(stack_list)
