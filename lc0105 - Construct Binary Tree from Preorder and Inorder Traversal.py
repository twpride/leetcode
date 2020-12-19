# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
      
      cache={v:ix for ix,v in enumerate(inorder)}
      
      def helper(lo,hi):
        if lo==hi:return
        rootval=preorder.pop(0)
        root= TreeNode(rootval)
        mid=cache[rootval]
        root.left=helper(lo,mid)
        root.right=helper(mid+1,hi)
        return root
      
      return helper(0,len(inorder))