# O(N) time and O(N) space complexity.

# Pseudocode:
# do level-by-level order traversal and based on pattern do the reverse of that level.

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        myqueue = []
        LOT_list = []
        zigzag_LOT_list = []
        node_list = []
        
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
            for idx,level_list in enumerate(LOT_list):
                if idx % 2 : #odd
                    zigzag_LOT_list.append(level_list[::-1])
                else:
                    zigzag_LOT_list.append(level_list)
        return zigzag_LOT_list
        
