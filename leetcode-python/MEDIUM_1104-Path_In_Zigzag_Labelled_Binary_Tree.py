# O(logN) solution

# Pseudocode:
# distance from node at the start to current node = mirror node's position from node at the end node of the same level.

import math
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
                
        num = label
        ans.append(num)
        while num != 1:
            # print(num)
            second_num = num // 2
            # print(second_num)
            low_log = int(math.floor(math.log2(second_num)))
            # print(low_log)
            second_num = (1 << low_log) + (1 << (low_log+1)) - second_num - 1
            # print(second_num)
            ans.append(second_num)
            num = second_num
        return ans[::-1]
