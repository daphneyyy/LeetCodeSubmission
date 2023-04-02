// Given a linked list, swap every two adjacent nodes and return its head. 
// You must solve the problem without modifying the values in the list's nodes 
// (i.e., only nodes themselves may be changed.)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode cur_node = head;
        ListNode next_node = head.next;
        ListNode res = next_node;
        while (next_node != null) {
            cur_node.next = next_node.next;
            next_node.next = cur_node;
            if (cur_node.next == null) {
                break;
            }
            if (cur_node.next.next == null) {
                break;
            }
            ListNode temp = cur_node.next;
            cur_node.next = temp.next;
            cur_node = temp;
            next_node = temp.next;
        }
        return res;
    }
}
