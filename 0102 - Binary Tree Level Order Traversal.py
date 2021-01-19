"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""
from typing import List


class Solution:
  # def levelOrder(self, root: TreeNode) -> List[List[int]]:
  #   q=deque()
  #   if root: 
  #     q.append(root)
  #   res=[]
  #   nq=[]
  #   while q:
  #     row=[]
  #     while q:
  #       t = q.popleft()
  #       row.append(t.val)
  #       if t and t.left:
  #         nq.append(t.left)
  #       if t and t.right:
  #         nq.append(t.right)
  #     q.extend(nq)
  #     nq=[]
  #     res.append(row)
  #   return res


  def levelOrder(self, root: TreeNode) -> List[List[int]]:

    def dfs(root,level):
      if not root: 
        return
      if level > len(res)-1: 
        res.append([])
      res[level].append(root.val)
      dfs(root.left, level+1)
      dfs(root.right, level+1)
      
    res=[]
    dfs(root,0)
    
    return res

s = Solution()

