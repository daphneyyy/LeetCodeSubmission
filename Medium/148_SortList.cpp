// Given the head of a linked list, return the list after sorting it in ascending order.
  
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeSort(ListNode* left, ListNode* right) {
        ListNode head(0);
        ListNode* temp = &head;
        while (left != NULL && right != NULL) {
            if (left->val < right->val) {
                temp->next = left;
                left = left->next;
            } else {
                temp->next = right;
                right = right->next;
            }
            temp = temp->next;
        }
        if (left != NULL) {
            temp->next = left;
        } else {
            temp->next = right;
        }
        return head.next;
    }

    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode* midPrev = head;
        ListNode* mid = head;
        ListNode* track = head;
        while (track && track->next) {
            midPrev = mid;
            mid = mid->next;
            track = track->next->next;
        }
        midPrev->next = nullptr;
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);
        return mergeSort(left, right);
    }
};
