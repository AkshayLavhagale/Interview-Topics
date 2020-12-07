# 1- whether two given tree are the same or not and 2 - if a given tree is subtree of another tree or not.
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
# subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
"""
Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s, t):

        if s is None and t is None:
            return True
        if t is None:
            return True
        if s is None:
            return False
        return self.issame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def issame(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.issame(s.left, t.left) and self.issame(s.right, t.right)


s = [3, 4, 1, 2, 5]
t = [4, 1, 2]

S = Solution()
print(S.isSubtree(s, t))
