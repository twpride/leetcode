"""
# Definition for a Node.
"""


class Node:

  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


class Solution:

  def cloneGraph(self, node: 'Node') -> 'Node':
    ss = dict()

    def dfs(n):
      if n.val in ss:
        return ss[n.val]
      else:
        ret = Node(val=n.val)
        ss[n.val] = ret

      for nn in n.neighbors:
        zz = dfs(nn)
        if zz:
          zz.neighbors.append(ret)

          # ret.neighbors.append(zz)/

      return ret

    if not node:
      return None
    return dfs(node)
