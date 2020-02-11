# O(N) time and O(N) space complexity

# implementation problem of Level order traversal using 'None' as delimiter

# why queue?
# because we need to process on some level as 'first in first order' on the current elements of queue

# why delimiter?
# because we want to return list of list of level-by-level order traversal,
# and having delimiter enables us to know when the level of previous level ended,
# so we can append node_list to ans_list and flush ans_list.

# Pseudocode:
# push 'root' and the delimiter 'None' into queue.
# while queue has more than 1 element ( not checking for queue being empty )
# pop it, and check whether delimiter is popped, and if queue is not empty, then append node_list to ans_list
# else, push it's left & right children, and append popped node to node_list
# at the end, queue will become empty, so append the node_list to ans_list.

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        myqueue = []
        ans_list = []
        node_list = []
        
        if root:
            # None as delimiter for 'end-of-level'
            myqueue.append(root)
            myqueue.append(None)

            # queue should have more than 1 element
            # because we are appending delimiter
            while len(myqueue) > 1:
                a = myqueue.pop(0)
                if a is None: #End of level
                    # Below is stopping condition. 
                    # queue should have more than 1 element bcoz if curr elem is None, and we pop it 
                    # and the queue is empty and we are appending None, this might cause inifnite loop unless 
                    # we check for queue is not empty.
                    if len(myqueue) > 0:
                        myqueue.append(None)
                        ans_list.append(node_list)
                        node_list = []
                else:
                    if a.left:
                        myqueue.append(a.left)
                    if a.right:
                        myqueue.append(a.right)
                    node_list.append(a.val)
            # last delimiter ke time queue will become empty, hence won't append to ans_list, 
            # bcoz we are appending only when it is delimiter and queue is not empty.
            if node_list:
                ans_list.append(node_list)
            del node_list
            del myqueue
        return ans_list
