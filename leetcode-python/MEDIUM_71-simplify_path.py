# O(N) time, O(N) space complexity
# split on '/'
# pop when you find '..'
# do nothing when you find '.'
# else push elements
# append with '/' at begin.

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        stack_list = []
        for elem in path_list:
            if elem:
                if elem == '..':
                    if len(stack_list):
                        a = stack_list.pop()
                elif elem == '.':
                    pass
                else:
                    stack_list.append(elem)
        ans_str = "/".join(stack_list)
        return "/"+ans_str
        
