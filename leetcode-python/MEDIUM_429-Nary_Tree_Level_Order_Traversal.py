# O(N) time and O(N) space complexity

# Pseudocode:
# same as level-by-level order traversal, but instead of left-right, we loop on a.children.

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                    for child in a.children:
                        if child:
                            myqueue.append(child)
                    node_list.append(a.val)
            if node_list:
                LOT_list.append(node_list)
        return LOT_list
