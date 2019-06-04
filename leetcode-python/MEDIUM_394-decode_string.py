# O(N) time and O(N) space complexity

# implementation problem of stack

# why stack?
# because we need to process on some level as 'last in first order' on the current elements of stack

# when you get ']', pop all alphabets in a string
# then after you get '[', pop all numbers in a string
# append in same stack

class Solution:
    def decodeString(self, s: str) -> str:
        stack_list = []
        for elem in s:
            if elem is ']':
                stri = ""
                while stack_list and stack_list[-1].isalpha():
                    a = stack_list.pop()
                    stri += a
                if stack_list[-1] == '[':
                    a = stack_list.pop()
                    num = ""
                    while stack_list and stack_list[-1].isnumeric():
                        b = stack_list.pop()
                        num += b
                    number = int(num[::-1])
                    str_rev = stri[::-1]
                    for i in range(number):
                        for el in str_rev:
                            stack_list.append(el)
            else:
                stack_list.append(elem)
        return "".join(stack_list)
