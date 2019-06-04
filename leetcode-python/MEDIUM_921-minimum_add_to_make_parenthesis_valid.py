# O(N) time and O(1) space complexity

# think about when we need to add parenthesis?
# one case is when balance is -ve, those elements will remain in stack
# last case is when at the end, if balance is +ve, it means it needed that much closing brakcets. 

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        balance = 0
        neg = 0
        for elem in S:
            if elem == '(':
                balance += 1
            elif elem == ')':
                if balance:
                    balance -= 1
                else:
                    neg += 1
        return balance+neg
