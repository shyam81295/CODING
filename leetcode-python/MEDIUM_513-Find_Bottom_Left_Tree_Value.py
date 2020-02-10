# O(N) time and O(N) space complexity.

# Pseudocode:
# do level-by-level order traversal and get last level's first node.

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        myqueue = []
        LOT_list = []
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
        if LOT_list:
            if LOT_list[-1]:
                return LOT_list[-1][0]
