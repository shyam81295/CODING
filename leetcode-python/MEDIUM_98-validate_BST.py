# O(N) time, O(N) space comeplexity
# checking all nodes -> O(N) time
# recursion stack might store for all O(N) nodes, fully skewed tree -> O(N) space

# Idea: each node will have floor & ceiling properties in BST
# if fails, then they are not BST.
class Solution:       
    def isValidBST(self, root: TreeNode, floor=float('-inf'), ceiling=float('inf')) -> bool:
        if not root:
            return True
        if not floor < root.val < ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return self.isValidBST(root.left,floor,root.val) and self.isValidBST(root.right,root.val,ceiling)
