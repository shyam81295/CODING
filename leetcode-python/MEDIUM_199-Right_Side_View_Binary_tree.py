# O(N) space and O(N) time complexity

# why level-order traversal?
# we want to get one node per level
# if we have level-by-level order traversal of tree, we can get Right side view.

# Pseudocode:
# do level-order traversal, and for each level return last node.

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        LOD_list = []
        node_list = []
        myqueue = []
        right_side_view_list = []
        
        if root:
            myqueue.append(root)
            myqueue.append(None)
            
            while len(myqueue) > 1:
                a = myqueue.pop(0)
                if a is None:
                    if myqueue:
                        myqueue.append(None)
                        LOD_list.append(node_list)
                        node_list = []
                else:
                    if a.left:
                        myqueue.append(a.left)
                    if a.right:
                        myqueue.append(a.right)
                    node_list.append(a.val)
            if node_list:
                LOD_list.append(node_list)
            del myqueue
            del node_list
        for level_list in LOD_list:
            if level_list:
                right_side_view_list.append(level_list[-1])
        del LOD_list
        return right_side_view_list
