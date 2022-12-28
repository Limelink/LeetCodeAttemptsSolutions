"""21. Merge Two Sorted Lists"""

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2) -> list:

        mergedList = list1 + list2
        mergedList.sort()
        print(mergedList)

        nodes = []
        for i in range(len(mergedList)):
            try:
                nodes.append(ListNode(mergedList[i], mergedList[i+1]))

            except IndexError:
                nodes.append(ListNode(mergedList[i], None))

            print(nodes[i].val, nodes[i].next)

        for node in nodes:
            if node.next is None:
                print(f"the Head of the list is: {node.val}")
                return node.val

solution = Solution()
solution.mergeTwoLists([1,2,4], [1,3,4])