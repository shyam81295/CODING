# O(N) time and O(N) space complexity using 1 stack.

# Pseudocode is same as Postorder Traversal (HARD_145 Leetcode)

# Questions/Intuitions to be pondered upon:
# 1. How to use if-else case for N-ary children when we want to append only 1 node from the children?
#       Loop the children, and use a flag for checking 
#       whether they are inside the loop or not
#       and when case of 'else' arises use the flag
# 2. How to know that this is the last child or not (to set curr node as visited) ?
#       Loop the children, and check whether node's idx == len(b.children)-1    [many more ways to get this done] 

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        mystack = []
        visited = {}
        postorder = []
        
        mystack.append(root)
        
        while mystack:
            curr = mystack[-1]
            if curr and not (curr in visited):
                is_in_loop = False
                for node in curr.children:
                    if node and not (node in visited):
                        mystack.append(node)
                        is_in_loop = True
                        break
                if not is_in_loop:
                    if mystack:
                        a = mystack.pop()
                        visited[a] = True
                        postorder.append(a.val)
                        if mystack:
                            b = mystack[-1]
                            for idx,node in enumerate(b.children):
                                if node == a and idx != len(b.children)-1:  # non-last child of b which is a
                                    mystack.append(b.children[idx+1])
                                elif node == a and idx == len(b.children)-1:    # last child of b which is a
                                    visited[b] = True
                                    postorder.append(b.val)
            else:
                if mystack:
                    mystack.pop()
        return postorder
        
