# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        new_cur = dummy_head

        cur = head.next
        while cur is not None:
            cur_sum = 0
            while cur.val != 0:
                cur_sum += cur.val
                cur = cur.next
            new_cur.next = ListNode(cur_sum)
            new_cur = new_cur.next
            cur = cur.next

        return dummy_head.next
