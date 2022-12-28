"""
LeetCode - 226. Invert Binary Tree
25.12.2022
"""

# Need to revisit! Recursion method is necessary skill!

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        pass

        binTree = []
        squares = [2**i for i in range(0, 7)]
        print(squares)

        i = 0
        while root:
            binTree += [root[:squares[i]]]
            root = root[squares[i]:]
            i += 1
            print(root)
            print(binTree)

        invertedTree = [item[::-1] for item in binTree]
        print(invertedTree)

        result = []
        for i in invertedTree:
            for j in invertedTree[i]:
                result.append(invertedTree[i][j])
        print(result)

        return


squares = [2**i for i in range(0, 7)]
root = [4,2,7,1,3,6,9]
new_root = []

# print(squares)
# print(root[:squares[0]])
# new_root += [root[:squares[0]]]
# print(new_root)
# root = root[squares[0]:]
# new_root += [root[:squares[1]]]
# print(new_root)
i = 0
while root:
    new_root += [root[:squares[i]]]
    root = root[squares[i]:]
    i += 1
    print(root)
    print(new_root)

new_root = [item[::-1] for item in new_root]
print(new_root)

result = []
for i in range(len(new_root)):
    for j in range(len(new_root[i])):
        result.append(new_root[i][j])
print(result)