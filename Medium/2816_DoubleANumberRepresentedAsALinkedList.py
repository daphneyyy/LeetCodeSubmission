# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            res = ListNode(1, head)
        else:
            res = head
        temp = head
        while temp != None:
            if temp.next != None and temp.next.val >= 5:
                temp.val = temp.val * 2 % 10 + 1 
            else:
                temp.val = temp.val * 2 % 10
            temp = temp.next
        return res
        
