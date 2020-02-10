# O(N) time and O(N) space complexity

# Pseudocode:
# do level-by-level traversal and find max of each level.

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        myqueue = []
        LOT_list = []
        node_list = []
        largest_in_each_row = []
        
        if root:
            myqueue.append(root)
            myqueue.append(None)
            
            while len(myqueue) > 1:
                a = myqueue.pop(0)
                if a is None:
                    if myqueue:
                        myqueue.append(None)
                        LOT_list.append(node_list)
                        node_list = []
                else:
                    if a.left:
                        myqueue.append(a.left)
                    if a.right:
                        myqueue.append(a.right)
                    node_list.append(a.val)
            if node_list:
                LOT_list.append(node_list)
            for level_list in LOT_list:
                max_value = float('-inf')
                for elem in level_list:
                    if elem > max_value:
                        max_value = elem
                largest_in_each_row.append(max_value)
        return largest_in_each_row
        
