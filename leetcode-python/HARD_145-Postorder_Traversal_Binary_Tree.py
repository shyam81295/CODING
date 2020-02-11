# O(N) time and O(h) space complexity using only 1 stack.

# In the below pseudocode context, visited means (visited as it would've been in postorder traversal)

# Pseudocode:
# 1. Append root to stack.
# 2. while stack is not empty:
# a.  curr = peek stack
# b.  if curr node is not visited:
#       if curr.left is not visited:
#         append curr.left to stack
#       elif curr.right is not visited:
#         append curr.right to stack
#       else:
#         a = stack.pop
#         visited[a] = True       <-- here we get our postorder traversal
#         b = stack.peek
#         if a is left child of b:
#           append b's right child to stack
#         elif a is right child of b:
#           visited[b] = True     <-- here we get our postorder traversal
# c.  else:
#       stack.pop

# Questions/Intuition that needed to be pondered upon for this solution:
# 1. Jo pop kiya woh left tha ya right?
# 2. How to make sure we don't visit the same node again when backtracking?
#     We need to make sure the nodes have visited attribute, 
#     so that we can pop/ignore them when backtracking.
# 3. We only need to push either the left child or right child 
#     but not both childs in stack at once.
# 4. When do we update visited attribute of node? 
#     (order of visited filling is equal to the order of the traversal you are doing)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        mystack = []
        visited = {}
        postorder = []
        
        mystack.append(root)
        
        while mystack:
            curr = mystack[-1]
            if curr and not (curr in visited):
                if curr.left and not (curr.left in visited):
                    mystack.append(curr.left)
                elif curr.right and not (curr.right in visited):
                    mystack.append(curr.right)
                else:
                    if mystack:
                        a = mystack.pop()
                        visited[a] = True
                        postorder.append(a.val)
                        if mystack:
                            b = mystack[-1]
                            if b.left == a:
                                mystack.append(b.right)
                            elif b.right == a:
                                visited[b] = True
                                postorder.append(b.val)
            else:
                if mystack:
                    mystack.pop()
        return postorder
        
        
