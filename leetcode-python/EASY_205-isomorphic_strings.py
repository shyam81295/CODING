# O(N) solution
# idea is to have bijection between 2 sets
# for bijection, we need to map each character with only 1 character.
# 2 maps and if character is already present then it should map to its previous value only. else no bijection.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        
        if len(s) != len(t):
            return False
        else:
            answer = True
            for i in range(len(s)):
                if s[i] not in mapping1:
                    mapping1[s[i]] = t[i]
                else:
                    if t[i] != mapping1[s[i]]:
                        answer = False
                        break
                if t[i] not in mapping2:
                    mapping2[t[i]] = s[i]
                else:
                    if s[i] != mapping2[t[i]]:
                        answer = False
                        break
            return answer
